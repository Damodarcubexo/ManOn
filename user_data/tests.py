# import unittest
#
# from django.urls import reverse
# from rest_framework.test import APIClient
# import json
# from rest_framework import status
# from .models import UserTable, Otp
# from .serializers import UserTableSerializer, AuthTokenSerializer, SetNewPasswordSerializer
#
#
# # Create your tests here.
#
#
# class RegisterApiTest(unittest.TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#     def testRegister(self):
#         # UserTable.objects.create(firstName="vikrant", lastName="shukla", email="lcy06shukla@gamil.com",
#         #                          password="vikrant@123", player_name="lcy", team_name="dc")
#         url = reverse('register')
#         response = self.client.get(url)
#
#         payload = {"firstName": "vikrant", "lastName": "shukla", "email": "lcy06shukla@gamil.com",
#                    "password": "vikrant@123", "player_name": "lcy", "team_name": "dc"}
#         self.client.post(response, payload)
#         self.assertEqual(response.status_code, 200)
