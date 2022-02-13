from user_data.models import UserTable
from user_data.tests.test_setup import TestSetUp
from faker import Faker

class Test_RegisterAPI(TestSetUp):
    """Api to store the new user details into database"""

    def test_post_cant_register(self):
        """so save the details and generating the user id"""

        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_post_can_register(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(response.status_code, 201)

    def test_user_cannot_login_with_unverified_email(self):
        response = self.client.post(self.login_url, self.user_data, format="json")
        self.assertAlmostEqual(response.status_code, 400, delta=400)

    def test_user_can_login_verified_email(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = UserTable.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertAlmostEqual(res.status_code, 201, delta=200)

