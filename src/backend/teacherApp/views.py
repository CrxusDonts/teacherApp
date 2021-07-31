from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Permission
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.utils import json

from .serializers import *


# status 请参考https://www.runoob.com/http/http-status-codes.html

class BackendAccountView(viewsets.ModelViewSet):
    queryset = BackendAccount.objects.all()
    serializer_class = BackendAccountSerializer
    permission_classes = [permissions.AllowAny]

    # 注册后台账户
    @action(methods=['post'], detail=False)
    def register_teacher(self, request):
        user_name = request.data.get('user_name')
        password = request.data.get('password')
        try:
            with transaction.atomic():
                response_str = 'User create '
                new_user = User.objects.create_user(username=user_name, password=password)
                response_str = 'Class create '
                clazz = register_class(request.data.get('class_name'))
                new_backend_account = BackendAccount.objects.create(user=new_user)
                response_str = 'Add permission '
                add_permission(new_backend_account)
                new_backend_account.save()
                response_str = 'Add manager '
                add_manager(True, new_backend_account, clazz)
        except IntegrityError:
            return Response('User already existed.')
        except Exception:
            return Response(response_str + 'failed.')
        return Response('Register succeed.')

    # 更改账户的密码
    @action(methods=['put'], detail=False)
    def change_password(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        cur_user = request.user
        if cur_user.check_password(old_password):
            try:
                cur_user.set_password(new_password)
                cur_user.save()
            except Exception:
                return Response('Modify password failed.')
        else:
            return Response('Old password is not correct.')
        return Response('Modify password succeed.')

    # 登陆
    @action(methods=['post'], detail=False)
    def login(self, request):
        try:
            user_name = request.data.get('user_name')
            password = request.data.get('password')
            user = authenticate(username=user_name, password=password)
            if user:
                login(request, user)
                return Response('Login succeed.')
            else:
                return Response('Login failed.')
        except Exception:
            return Response(status=500)

    # 登出
    @action(methods=['post'], detail=False)
    def logout(self, request):
        try:
            logout(request)
            return Response('logout succeed.')
        except Exception:
            return Response('logout failed.')


class ClassView(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    # 添加作业
    @action(methods=['post'], detail=True)
    def new_homework(self, request, pk):
        try:
            clazz = Class.objects.get(id=pk)
        except Exception:
            return Response('Class not found.')
        title = request.data.get('title')
        start_time = request.data.get('start_time')
        due_time = request.data.get('due_time')
        repeatable = request.data.get('repeatable')
        homework = Homework.objects.create(title=title, start_time=start_time, due_time=due_time,
                                           repeatable=repeatable, clazz=clazz)
        homework.save()
        return Response('New homework succeed.')

    # 获取班级的作业
    @action(methods=['get'], detail=True)
    def get_homeworks(self, request, pk):
        try:
            clazz = Class.objects.get(id=pk)
        except Exception:
            return Response('Class not found.')
        homework_list = []
        for homework in Homework.objects.filter(clazz=clazz):
            homework_list.append(homework)
        serializer = HomeworkSerializer(homework_list, many=True)
        return Response(serializer.data)

    # 获取我的班级
    @action(methods=['get'], detail=False)
    def get_my_class(self, request):
        try:
            cur_user = request.user
            cur_account = BackendAccount.objects.get(user=cur_user)
            clazz = cur_account.account_manager.get(is_owner=True).clazz
            serializer = ClassSerializer(clazz)
            return Response(serializer.data)
        except Exception:
            return Response('Get my own class failed.')

    # 获取我管理的（除了我的班级）班级列表
    @action(methods=['get'], detail=False)
    def get_manage_class_list(self, request):
        try:
            cur_user = request.user
            cur_account = BackendAccount.objects.get(user=cur_user)
            class_list = []
            for manager in cur_account.account_manager.all().filter(is_owner=False):
                class_list.append(manager.clazz)
            serializer = ClassSerializer(class_list, many=True)
            return Response(serializer.data)
        except Exception:
            return Response('Get my manage class failed.')


class ManagerView(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    @action(methods=['post'], detail=False)
    def get_teacher(self, request):
        try:
            cur_class_id = request.data.get('class_id')
            cur_class = Class.objects.get(id=cur_class_id)
            cur_user = request.user
            manager_list = []
            for manager in cur_class.class_manager.all():
                if manager.account.user != cur_user:
                    data = json.dumps({
                        'id': manager.account.id,
                        'username': manager.account.user.username
                    })
                    manager_list.append(data)
            return Response(manager_list)
        except Exception:
            return Response('get_teacher failed.')


class FrontAccountView(viewsets.ModelViewSet):
    queryset = FrontAccount.objects.all()
    serializer_class = FrontAccountSerializer


class PeopleView(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer


class ChoiceQuestionView(viewsets.ModelViewSet):
    queryset = ChoiceQuestion.objects.all()
    serializer_class = ChoiceQuestionSerializer


class OptionsView(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

    @action(methods=['post'], detail=True)
    def add_option(self, request, pk):
        try:
            question = ChoiceQuestion.objects.get(id=pk)
            text_content = request.data.get('text_content')
            order = request.data.get('order')
            if_correct = request.data.get('if_correct')
            new_options = Options.objects.create \
                (question=question, text_content=text_content, order=order, if_correct=if_correct)
            new_options.save()
            return Response('add_option succeed.')
        except Exception:
            return Response('add_option failed.')

    @action(methods=['get'], detail=True)
    def get_options(self, request, pk):
        try:
            question = ChoiceQuestion.objects.get(id=pk)
            option_list = []
            for option in question.question_option.all().order_by('order'):
                option_list.append(option.text_content)
            return Response(option_list)
            pass
        except Exception as e:
            return Response('get_options failed.')


class ChoiceQuestionUserAnswerView(viewsets.ModelViewSet):
    queryset = ChoiceQuestionUserAnswer.objects.all()
    serializer_class = ChoiceQuestionUserAnswerSerializer


class MediaView(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

    @action(methods=['get'], detail=False)
    def test_get(self, request):
        try:
            media = Media.objects.get(id=12)
            file = media.file
            return Response(file)
        except Exception as e:
            return Response(str(e))


class HomeworkView(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

    # 添加选择题
    @action(methods=['post'], detail=True)
    def new_choice_question(self, request, pk):
        try:
            homework = Homework.objects.get(id=pk)
        except Exception:
            return Response('Homework not found.')
        text_content = request.data.get('text_content')
        choice_question = ChoiceQuestion.objects.create(text_content=text_content, homework=homework)
        choice_question.save()
        return Response(choice_question.id)

    # 添加填空题
    @action(methods=['post'], detail=True)
    def new_completion_question(self, request, pk):
        try:
            homework = Homework.objects.get(id=pk)
        except Exception:
            return Response('Homework not found.')
        text_content = request.data.get('text_content')
        completion_question = CompletionQuestion.objects.create(text_content=text_content, homework=homework)
        completion_question.save()
        return Response('New completion question succeed.')

    # 添加主观题
    @action(methods=['post'], detail=True)
    def new_subjective_question(self, request, pk):
        try:
            homework = Homework.objects.get(id=pk)
        except Exception:
            return Response('Homework not found.')
        text_content = request.data.get('text_content')
        subjective_question = SubjectiveQuestion.objects.create(text_content=text_content, homework=homework)
        subjective_question.save()
        return Response('New subjective question succeed.')

    # 获取选择题
    @action(methods=['get'], detail=True)
    def get_choice_question(self, request, pk):
        try:
            choice_question_list = get_question(pk=pk, question_type='choice_question')
        except Exception:
            return Response('Homework not found.')
        serializer = ChoiceQuestionSerializer(choice_question_list, many=True)
        return Response(serializer.data)

    # 获取填空题
    @action(methods=['get'], detail=True)
    def get_completion_question(self, request, pk):
        try:
            completion_question_list = get_question(pk=pk, question_type='completion_question')
        except Exception:
            return Response('Homework not found.')
        serializer = ChoiceQuestionSerializer(completion_question_list, many=True)
        return Response(serializer.data)

    # 获取主观题
    @action(methods=['get'], detail=True)
    def get_subjective_question(self, request, pk):
        try:
            subjective_question_list = get_question(pk=pk, question_type='subjective_question')
        except Exception:
            return Response('Homework not found.')
        serializer = SubjectiveQuestionSerializer(subjective_question_list, many=True)
        return Response(serializer.data)


class CompletionQuestionView(viewsets.ModelViewSet):
    queryset = CompletionQuestion.objects.all()
    serializer_class = CompletionQuestionSerializer


class CompletionQuestionAnswerView(viewsets.ModelViewSet):
    queryset = CompletionQuestionAnswer.objects.all()
    serializer_class = CompletionQuestionAnswerSerializer


class CompletionQuestionUserAnswerView(viewsets.ModelViewSet):
    queryset = CompletionQuestionUserAnswer.objects.all()
    serializer_class = CompletionQuestionUserAnswerSerializer


class SubjectiveQuestionView(viewsets.ModelViewSet):
    queryset = SubjectiveQuestion.objects.all()
    serializer_class = SubjectiveQuestionSerializer


class SubjectiveQuestionUserAnswerView(viewsets.ModelViewSet):
    queryset = SubjectiveQuestionUserAnswer.objects.all()
    serializer_class = SubjectiveQuestionUserAnswerSerializer


class TeacherCommentView(viewsets.ModelViewSet):
    queryset = TeacherComment.objects.all()
    serializer_class = TeacherCommentSerializer


class JoinClassRequestView(viewsets.ModelViewSet):
    queryset = TeacherComment.objects.all()
    serializer_class = TeacherCommentSerializer


class ManageInvitationView(viewsets.ModelViewSet):
    queryset = ManageInvitation.objects.all()
    serializer_class = ManageInvitationSerializer

    @action(methods=['post'], detail=False)
    def invite_assistant(self, request):
        try:
            inviter = BackendAccount.objects.get(user=request.user)
            invitee = BackendAccount.objects.get(user=User.objects.get(username=request.data.get('user_name')))
            clazz = Class.objects.get(id=request.data.get('class_id'))
            new_invitation = ManageInvitation.objects.create(inviter=inviter, invitee=invitee, clazz=clazz)
            new_invitation.save()
            return Response('invite succeed.')
        except Exception:
            return Response('invite failed.')

    @action(methods=['get'], detail=False)
    def get_invitation(self, request):
        try:
            cur_account = BackendAccount.objects.get(user=request.user)
            invitation_list = []
            for invitation in cur_account.account_invitee.all():
                invitation_list.append(invitation)
            serializer = ManageInvitationSerializer(invitation_list, many=True)
            return Response(serializer.data)
        except Exception:
            return Response('get_invitation failed.')

    @action(methods=['post'], detail=False)
    def handle_invitation(self, request):
        try:
            if_accept = request.data.get('if_accept')
            invitation_id = request.data.get('invitation_id')
            invitation = ManageInvitation.objects.get(id=invitation_id)
            if if_accept:
                clazz = invitation.clazz
                account = invitation.invitee
                new_manager = Manager.objects.create(is_owner=False, clazz=clazz, account=account)
                new_manager.save()
            invitation.delete()
            return Response('handle_invitation succeed.')
        except Exception:
            return Response('handle_invitation failed.')


# 用于注册班级的方法
def register_class(name):
    class_name = name
    try:
        new_class = Class.objects.create(class_name=class_name)
        new_class.save()
    except Exception:
        raise Exception
    return new_class


# 用于添加manager表的方法
def add_manager(is_owner, account, class_name):
    try:
        new_manager = Manager.objects.create(is_owner=is_owner, account=account, clazz=class_name)
        new_manager.save()
    except Exception:
        raise Exception


# 用于对用户添加权限的方法
def add_permission(backend_account):
    permission_list = Permission.objects.filter(id__gt=24).all()  # 24及24以前均为后台admin管理权限
    for permission in permission_list:
        backend_account.user.user_permissions.add(permission)


# 用于返回作业的方法
def get_question(pk, question_type):
    try:
        homework = Homework.objects.get(id=pk)
    except Exception:
        raise Exception
    question_list = []
    if question_type == 'choice_question':
        for choice_question in ChoiceQuestion.objects.filter(homework=homework):
            question_list.append(choice_question)
    elif question_type == 'completion_question':
        for completion_question in CompletionQuestion.objects.filter(homework=homework):
            question_list.append(completion_question)
    elif question_type == 'subjective_question':
        for subjective_question in SubjectiveQuestion.objects.filter(homework=homework):
            question_list.append(subjective_question)
    return question_list


# 用于保存媒体文件的方法
def save_media(request):
    try:
        with transaction.atomic():
            file_type = request.data.get('file_type')
            file = request.FILES.get('file')
            if not file:
                raise Exception
            if file_type == 'image':
                new_media = Media.objects.create(file=file, file_type=0)
            elif file_type == 'video':
                new_media = Media.objects.create(file=file, file_type=1)
            elif file_type == 'voice':
                pass  # TODO:实现存储音频的方法（等待具体明确音频格式）
            new_media.save()
            return new_media
    except Exception:
        return 'failed.'
