# tests/test_apis.py
import json
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class PokeballImgTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_pokeball_img_api_view(self):
        ball = 'pokeball'
        thumbnail_url = "https://example.com/image.png"

        class MockObject():
            status_code = 200
            json = lambda _: {'icons': [{"thumbnail_url": thumbnail_url}]}

        patch('requests.get', Mock(return_value=MockObject())).start()

        result = self.client.get(reverse('pokeball', args=[ball]))

        self.assertEquals(json.loads(result.content), {"thumbnail": thumbnail_url})