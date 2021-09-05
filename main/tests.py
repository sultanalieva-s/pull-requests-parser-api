import json

from django.test import TestCase, Client
from django.urls import reverse

client = Client()

# Create your tests here.


class PullRequestsTestCases(TestCase):

    def setUp(self) -> None:
        self.endpoint = reverse('pullrequests')

        self.valid_github_link = 'https://github.com/sehmaschine/django-grappelli'
        self.not_valid_github_link_1 = 'https://github.com/sehmaschine/asasasas'
        self.not_valid_github_link_2 = 'asasas'
        self.not_valid_github_link_3 = 'https://github.com/'
        self.not_valid_github_link_4 = 'https://github.com/sehmaschine/'
        self.not_valid_github_link_5 = 'https://www.django-rest-framework.org/api-guide/testing/'

    def test_response_pull_requests_view(self):
        response = client.post(self.endpoint, json.dumps({'github_link': self.valid_github_link}),
                               content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_github_link_validation_1(self):
        response = client.post(self.endpoint, json.dumps({'github_link': self.not_valid_github_link_1}),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_github_link_validation_2(self):
        response = client.post(self.endpoint, json.dumps({'github_link': self.not_valid_github_link_2}),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_github_link_validation_3(self):
        response = client.post(self.endpoint, json.dumps({'github_link': self.not_valid_github_link_3}),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_github_link_validation_4(self):
        response = client.post(self.endpoint, json.dumps({'github_link': self.not_valid_github_link_4}),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_github_link_validation_5(self):
        response = client.post(self.endpoint, json.dumps({'github_link': self.not_valid_github_link_5}),
                               content_type='application/json')

        self.assertEqual(response.status_code, 400)

# TODO Add more tests: for parsing logic and database
