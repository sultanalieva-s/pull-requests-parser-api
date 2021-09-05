import json

from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
# TODO: Add tests


class PullRequestsTestCases(TestCase):

    def setUp(self) -> None:
        pass

    def test_response_pull_requests_view(self):
        url = reverse('pullrequests')
        print('URL: ' + url)

        data = {'github_link': 'https://github.com/sehmaschine/django-grappelli'}
        response = self.client.post(url, json.dumps({'title': 'new idea'}), content_type='application/json')

        print(response)

        self.assertEqual(response.status_code, 201)



