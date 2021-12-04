from .models import Poll, Question, Reply
from .serializers import PollSerializer, QuestionSerializer, ReplySerializer
from .permissions import PollPermission, QuestionPermission
from rest_framework import viewsets, mixins
from django.contrib.auth.models import User

class PollViewSet(viewsets.ModelViewSet):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()
    permission_classes = PollPermission,


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = QuestionPermission,


class ReplyViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = ReplySerializer
    queryset = Reply.objects.all()

    def get_queryset(self):
        query = self.queryset
        if self.request.user.is_superuser:
            return query

        if self.request.user.is_authenticated:
            query = query.filter(user=self.request.user)
            return query

        return query.none()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(user=self.request.user)

        self.request.session.save()
        username = str(self.request.session.session_key)
        try:
            user = User.objects.create_user(username)
        except:
            user = User.objects.get(email=username)
        return serializer.save(user=user)

