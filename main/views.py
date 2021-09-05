# Create your views here.
import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView

from main.models import PullRequest
from main.serializers import UserRequestSerializer, UserRequestResultSerializer, PullRequestSerializer
from rest_framework.response import Response
from rest_framework import status

from main.utils import parse_pull_requests


class PullRequestView(APIView):

    @swagger_auto_schema(responses={200: PullRequestSerializer(many=True)}, request_body=UserRequestSerializer)
    def post(self, request):
        github_link = request.data
        user_request_serializer = UserRequestSerializer(data=github_link)

        if user_request_serializer.is_valid(raise_exception=True):
            user_request = user_request_serializer.save()
            github_repo_html = requests.get(github_link['github_link']).text
            user_request_result_serializer = UserRequestResultSerializer(data={'github_response': github_repo_html, 'user_request': user_request.id})

            if user_request_result_serializer.is_valid(raise_exception=True):
                user_request_result = user_request_result_serializer.save()
                pull_requests_data = parse_pull_requests(user_request_result.github_response)

                for pull_request_data in pull_requests_data:
                    pull_request_serializer = PullRequestSerializer(data={'user_request': user_request.id,
                                                                          'user_request_result': user_request_result.id,
                                                                          'pull_request_title': pull_request_data['title'],
                                                                          'pull_request_link': pull_request_data['link'],
                                                                          'assignees': pull_request_data['assignees'],
                                                                          'reviewers': pull_request_data['reviewers'],
                                                                          })

                    if pull_request_serializer.is_valid(raise_exception=True):
                        pull_request_serializer.save()

                pull_requests = PullRequest.objects.filter(user_request=user_request.id)
                pull_requests_serializer = PullRequestSerializer(pull_requests, many=True)

                return Response(pull_requests_serializer.data, status=status.HTTP_201_CREATED)
