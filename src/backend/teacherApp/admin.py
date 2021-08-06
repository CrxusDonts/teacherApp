from django.contrib import admin
from .models import BackendAccount, Class, Manager, People, Options, ChoiceQuestion, ChoiceQuestionUserAnswer, Media, \
    Homework, CompletionQuestion, CompletionQuestionAnswer, SubjectiveQuestion, CompletionQuestionUserAnswer, \
    SubjectiveQuestionUserAnswer, TeacherComment, JoinClassRequest, ManageInvitation

admin.site.register(BackendAccount)
admin.site.register(Class)
admin.site.register(Manager)
admin.site.register(People)
admin.site.register(ChoiceQuestion)
admin.site.register(Options)
admin.site.register(ChoiceQuestionUserAnswer)
admin.site.register(Media)
admin.site.register(Homework)
admin.site.register(CompletionQuestion)
admin.site.register(CompletionQuestionAnswer)
admin.site.register(CompletionQuestionUserAnswer)
admin.site.register(SubjectiveQuestion)
admin.site.register(SubjectiveQuestionUserAnswer)
admin.site.register(TeacherComment)
admin.site.register(JoinClassRequest)
admin.site.register(ManageInvitation)
