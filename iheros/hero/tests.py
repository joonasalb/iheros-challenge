from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from iheros.user.models import User
import json

from iheros.user.serializers import (
    UserSerializer
)

from iheros.hero.serializers import (
    HeroSerializer,
)


class herorTests(APITestCase, TestCase):

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

        self.valid_hero_create_payload = {
            "latitude": 53.62447915751702, 
            "longitude": -2.293004904058518,
            "name": "criado agr",
            "rank": "C"
        }

        self.invalid_hero_create_payload = {
            "latitude": 53.62447915751702, 
            "name": "criado agr",
            "rank": "Z"
        }

        self.valid_hero_update_payload = {             
            "latitude": 0.21,
            "longitude": 0.21,
            "name": "ddasddas",
            "rank": "A"        
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

        # test hero payload

        url = '/api/hero/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(
            url, self.valid_hero_create_payload, format='json')
        self.test_flight_route = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        test_hero = HeroSerializer(
            data=self.valid_hero_create_payload)
        self.assertTrue(test_hero.is_valid())
        self.test_hero = test_hero.save()

    def test_authentication_success(self):
        """
        Test authentication success
        Correct: Status code 200
        """

        url = '/api/token'
        response = self.client.post(url, self.valid_user_login_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_heros(self):
        """
        test_list_heros
        Correct: Status code 200
        """

        url = '/api/hero/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_create_hero_failed(self):
        """
        Test create hero failed
        Correct: Status code 400
        """

        url = '/api/hero/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(
            url, self.invalid_hero_create_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_hero_success(self):
        """
        test create hero success
        Correct: Status code 200
        """

        url = '/api/hero/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(
            url, self.valid_hero_create_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_hero_not_found(self):
        """
        Test get hero not found
        Correct: Status code 404
        """

        url = '/api/hero/0/'
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_hero_by_id(self):
        """
        Test get hero by id
        Correct: Status code 200
        """

        url = '/api/hero/{}/'.format(self.test_hero.id)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_hero(self):
        """
        Test delete inspection
        Correct: Status code 204
        """

        url = '/api/hero/{}/'.format(self.test_hero.id)
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
 