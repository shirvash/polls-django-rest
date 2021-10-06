from rest_framework import serializers

from polls.models import Poll, Question, Choice, Reply, Answer


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text')
        read_only_fields = ('id',)


class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=Question.Type.choices, default=Question.Type.TEXT
    )
    choices = ChoiceSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'text', 'type', 'choices')
        read_only_fields = ('id',)


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ('id', 'title', 'date_start', 'date_end', 'is_active', 'questions')
        read_only_fields = ('id', 'date_start', 'is_active')


class AnswerSerializer(serializers.ModelSerializer):
# Текст иил Вариант ответа на выбор. Поле текста не должно быть requied
    class Meta:
        model = Answer
        fields = ('id', 'text', 'choice_id', 'question_id')


class ReplySerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Reply
        fields = ('id', 'user', 'poll',  'date_reply', 'answers')
        read_only_fields = ('user',)

    def create(self, validated_data):
        answers = validated_data.pop('answers', [])
        instance = Reply.objects.create(**validated_data)
        Answer.objects.bulk_create([
            Answer(reply=instance, **a) for a in answers
        ])
        return instance