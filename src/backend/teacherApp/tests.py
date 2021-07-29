import json
from django.contrib.auth.models import User

from django.test import TestCase


class BackendAccountViewTest(TestCase):
    def setUp(self):
        self.user_name = 'test'
        self.password = 'password4test'
        self.class_name = 'class4test'

    def test_register_teacher(self):
        test_data = json.dumps({
            'user_name': self.user_name,
            'password': self.password,
            'class_name': self.class_name
        })
        response = self.client. \
            post(path='http://localhost:8002/teacherApp/BackendAccount/register_teacher/',
                 data=test_data, content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        User.objects.create_user(username=self.user_name, password=self.password)
        self.client.login(username=self.user_name, password=self.password)
        test_data = json.dumps({
            'old_password': self.password,
            'new_password': '123456'
        })
        response = self.client. \
            put(path='http://localhost:8002/teacherApp/BackendAccount/change_password/',
                data=test_data, content_type='application/json')
        print(response.data)
        self.assertEqual(response.status_code, 200)
