from django.test import TestCase
from .forms import RegisterUserForm
import tempfile

class RegisterUserFormTest(TestCase):
    def test_register_form_is_valid(self):
        form = RegisterUserForm(
            data={
                'username': 'Test123',
                'password': '123456test',
                'email': 'testuser@gmail.com',
                'profile_pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertTrue(form.is_valid())

    def test_register_form_is_valid(self):
        form = RegisterUserForm(
            data={
                'username': 'Test123',
                'password': '123456test',
                'email': 'testuser@gmail.com',
                'profile_pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertTrue(form.is_valid())

    def test_register_form_username_is_not_valid(self):
        form = RegisterUserForm(
            data={
                'username': 'Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123Test123',
                'password': '123456test',
                'email': 'testuser@gmail.com',
                'profile_pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertFalse(form.is_valid())

    def test_register_form_password_is_not_valid(self):
        form = RegisterUserForm(
            data={
                'username': 'Test123',
                'password': '',
                'email': 'testuser@gmail.com',
                'profile_pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertFalse(form.is_valid())

    def test_register_form_email_is_not_valid(self):
        form = RegisterUserForm(
            data={
                'username': 'Test123',
                'password': '123456test',
                'email': 'testusergmail.com',
                'profile_pic': tempfile.NamedTemporaryFile(suffix=".jpg").name
            }
        )

        self.assertFalse(form.is_valid())

