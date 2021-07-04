from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """
        test creating a new user with email successful.
        """
        email = "test@aktweb.in"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
         Test the email for new user is normlized
        """
        email = "test@AKTWEB.in"
        user = get_user_model().objects.create_user(email=email, password='test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
        Test if email is given or not
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='test123')

    def test_create_super_user(self):
        """
        test create super user
        """
        user = get_user_model().objects.create_superuser(
            email='test@aktweb.in',
            password='pas123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
