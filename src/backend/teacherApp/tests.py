import json

from django.contrib.auth.models import User
from django.test import TestCase
from teacherApp.models import Class
from teacherApp.views import register_class, auto_register_student_account

type_json = 'application/json'
test_email = '1291923247@qq.com'


class BackendAccountViewTest(TestCase):
    def setUp(self):
        self.user_name = 'test'
        self.password = 'password4test'
        self.class_name = 'class4test'
        self.base_url = 'http://localhost:8002/teacherApp/BackendAccount/'

    def test_register_teacher(self):
        test_data = json.dumps({
            'user_name': self.user_name,
            'password': self.password,
            'class_name': self.class_name,
            'name': 'test_name'
        })
        response = self.client. \
            post(path=self.base_url + 'register_teacher/',
                 data=test_data, content_type=type_json)
        self.assertEqual(response.data, 'Register succeed.')

    def test_login(self):
        test_data = json.dumps({
            'user_name': self.user_name,
            'password': self.password
        })
        response = self.client. \
            post(path=self.base_url + 'login/', data=test_data, content_type=type_json)
        self.assertEqual(response.data, 'Login failed.')

    def test_change_password(self):
        User.objects.create_user(username=self.user_name, password=self.password)
        self.client.login(username=self.user_name, password=self.password)
        test_data = json.dumps({
            'old_password': self.password,
            'new_password': '123456'
        })
        response = self.client. \
            put(path=self.base_url + 'change_password/',
                data=test_data, content_type=type_json)
        self.assertEqual(response.data, 'Modify password succeed.')

    def test_logout(self):
        test_data = json.dumps({
            'user_name': self.user_name,
            'password': self.password
        })
        response = self.client. \
            post(path=self.base_url + 'logout/', data=test_data, content_type=type_json)
        self.assertEqual(response.data, 'logout succeed.')


class ClassViewTest(TestCase):
    def setUp(self):
        self.user_name = 'test'
        self.password = 'password4test'
        self.class_name = 'class4test'
        self.base_url = 'http://localhost:8002/teacherApp/Class/'
        User.objects. \
            create_superuser(username=self.user_name, password=self.password, email=test_email)
        self.client.login(username=self.user_name, password=self.password)
        self.clazz = Class.objects.create(class_name=self.class_name)
        self.clazz.save()

    def test_new_homework(self):
        test_data = json.dumps({
            'title': 'test_title'
        })
        response = self.client. \
            post(path=self.base_url + '1/new_homework/', data=test_data, content_type=type_json)
        self.assertEqual(response.data, 'Class not found.')

    def test_get_homeworks(self):
        response = self.client. \
            get(path=self.base_url + '1/get_homeworks/', content_type=type_json)
        self.assertEqual(response.data, 'Class not found.')

    def test_get_my_class(self):
        response = self.client. \
            get(path=self.base_url + 'get_my_class/', content_type=type_json)
        self.assertEqual(response.data, 'Get my own class failed.')

    def test_get_manage_class_list(self):
        response = self.client. \
            get(path=self.base_url + 'get_manage_class_list/', content_type=type_json)
        self.assertEqual(response.data, 'Get my manage class failed.')


class ManagerViewTest(TestCase):
    def setUp(self):
        self.user_name = 'test1'
        self.password = 'password4test1'
        self.class_name = 'class4test1'
        self.base_url = 'http://localhost:8002/teacherApp/'
        User.objects. \
            create_superuser(username=self.user_name, password=self.password, email=test_email)
        self.client.login(username=self.user_name, password=self.password)

    def test_get_teacher(self):
        test_data = json.dumps({
            'user_name': self.user_name,
            'password': self.password,
            'class_name': self.class_name
        })
        self.client. \
            post(path=self.base_url + 'BackendAccount/register_teacher/',
                 data=test_data, content_type=type_json)
        test_data = json.dumps({
            'class_id': 1
        })
        response = self.client. \
            post(path=self.base_url + 'Manager/get_teacher/',
                 data=test_data, content_type=type_json)
        self.assertEqual(response.status_code, 200)


class InterfaceTest(TestCase):
    def setUp(self):
        self.user_name = 'test2'
        self.password = 'password4test2'
        self.class_name = 'class4test2'
        self.base_url = 'http://localhost:8002/teacherApp/'
        self.user = User.objects. \
            create_superuser(username=self.user_name, password=self.password, email=test_email)
        self.client.login(username=self.user_name, password=self.password)

    def test_register_class(self):
        clazz = register_class(self.class_name)
        self.assertEqual(clazz.class_name, self.class_name)

    def test_register_student_account(self):
        account = auto_register_student_account('123456789')
        self.assertEqual(account.open_id, '123456789')
