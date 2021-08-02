from django.conf.urls.static import static
from django.urls import path, include

from api import settings
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('BackendAccount', views.BackendAccountView)
router.register('Class', views.ClassView)
router.register('Manager', views.ManagerView)
router.register('FrontAccount', views.FrontAccountView)
router.register('People', views.PeopleView)
router.register('ChoiceQuestion', views.ChoiceQuestionView)
router.register('Options', views.OptionsView)
router.register('ChoiceQuestionUserAnswer', views.ChoiceQuestionUserAnswerView)
router.register('Homework', views.HomeworkView)
router.register('Media', views.MediaView)
router.register('CompletionQuestion', views.CompletionQuestionView)
router.register('CompletionQuestionAnswer', views.CompletionQuestionAnswerView)
router.register('CompletionQuestionUserAnswer', views.CompletionQuestionUserAnswerView)
router.register('SubjectiveQuestion', views.SubjectiveQuestionView)
router.register('TeacherComment', views.TeacherCommentView)
router.register('JoinClassRequest', views.JoinClassRequestView)
router.register('ManageInvitation', views.ManageInvitationView)

urlpatterns = [
    path('', include(router.urls)),
]
