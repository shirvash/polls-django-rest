from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include

from polls.views import PollViewSet, QuestionViewSet, ReplyViewSet

router = SimpleRouter()
router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)
router.register('reply', ReplyViewSet)

urlpatterns = [

]

urlpatterns += router.urls