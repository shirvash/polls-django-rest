from rest_framework import serializers

from polls.fields import ObjectIDField
from polls.models import Poll, Question, Choice, Reply, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text')
        read_only_fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=Question.Type.choices, default=Question.Type.TEXT
    )
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'question_text', 'type', 'choices')
        read_only_fields = ('id',)


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'date_start', 'date_end', 'is_active', 'questions')
        read_only_fields = ('id', 'date_start', 'is_active')


class AnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(read_only=True)
    choice_id = ObjectIDField(queryset=Choice.objects.all(), write_only=True, allow_null=True)

    question = QuestionSerializer(read_only=True)
    question_id = ObjectIDField(queryset=Question.objects.all(), write_only=True, allow_null=True)

    class Meta:
        model = Answer
        fields = ('id', 'question_id', 'question', 'text', 'choice_id', 'choice')
        read_only_fields = ('id', 'question', 'choice')


class ReplySerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Reply
        fields = ('id', 'user', 'poll', 'date_reply', 'answers')
        read_only_fields = ('id', 'user', 'date_reply')

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])
        instance = Reply.objects.create(**validated_data)
        Answer.objects.bulk_create([
            Answer(reply=instance, **a) for a in answers
        ])
        return instance
