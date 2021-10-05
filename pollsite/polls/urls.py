from django.urls import path
from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include

from polls.views import PollViewSet, QuestionViewSet

router = SimpleRouter()
router.register('polls', PollViewSet)
router.register('questions', QuestionViewSet)

urlpatterns = [

]

urlpatterns += router.urls