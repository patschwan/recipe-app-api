from django.test import TestCase, Client  # Client allows to test app
from django.contrib.auth import get_user_model
from django.urls import reverse  # generate url for django admin page


class AdminSiteTest(TestCase):

    # setup function is a function that runs before test
    def setUp(self):
        # a client user to perform actions
        self.client = Client()
        # the admin user
        self.admin_user = get_user_model().objects.create_superuser(
            email='test123@test.de',
            password='password123'
        )
        # log in the admin user
        self.client.force_login(self.admin_user)

        # a normal user for testing purpose
        self.user = get_user_model().objects.create_user(
            email='test@test.de',
            password='test123',
            name='Testname'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')  # look up in docs
        res = self.client.get(url)  # response: test clients performs HTTP GET

        # assertContains checks if it contains AND other things like HTTP 200
        # look up in the docs
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user added page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/<user_id>
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
