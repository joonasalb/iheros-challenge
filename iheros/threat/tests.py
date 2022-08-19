from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from iheros.user.models import User
import json

from iheros.user.serializers import (
    UserSerializer
)

from iheros.threat.serializers import (
    ThreatSerializer,
)


class threatrTests(APITestCase, TestCase):

    def setUp(self):
        """
        Set up from tests
        """

        self.valid_user_create_payload = {
            "first_name": "teste",
            "last_name": "teste",
            "email": "teste@teste.com",
            "username": "teste",
            "password": "teste123",
        }

        self.valid_threat_create_payload = {
            "danger_level": "Wolf",
            "monster_name": "dsadsa",
            "location": {
                "latitude": -5.836597,
                "longitude": -35.236007
            }
        }

        self.invalid_threat_create_payload = {
            "danger_level": "Wolf_err",
            "monster_name": None,
            "location": {
                "latitude": 600.836597,
                "longitude": -35.236007
            }
        }

        test_user = UserSerializer(data=self.valid_user_create_payload)
        self.assertTrue(test_user.is_valid())
        self.test_user = User.objects.create_user(
            first_name="teste",
            last_name="teste",
            email="teste@teste.com",
            username="teste",
            password="teste123",
        )

        self.valid_user_login_payload = {
            "username": "teste",
            "password": "teste123",
        }

        url = '/api/token'
        response = self.client.post(url, self.valid_user_login_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.access_token = response.data["access"]

        # test threat payload

        url = '/api/threat/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(
            url, self.valid_threat_create_payload, format='json')
        self.test_flight_route = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        test_threat = ThreatSerializer(
            data=self.valid_threat_create_payload)
        self.assertTrue(test_threat.is_valid())
        self.test_threat = test_threat.save()

    def test_authentication_success(self):
        """
        Test authentication success
        Correct: Status code 200
        """

        url = '/api/token'
        response = self.client.post(url, self.valid_user_login_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_threats(self):
        """
        test_list_threats
        Correct: Status code 200
        """

        url = '/api/threat/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_create_threat_failed(self):
        """
        Test create threat failed
        Correct: Status code 400
        """

        url = '/api/threat/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(
            url, self.invalid_threat_create_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_threat_success(self):
        """
        test create threat success
        Correct: Status code 200
        """

        url = '/api/threat/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(
            url, self.valid_threat_create_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
