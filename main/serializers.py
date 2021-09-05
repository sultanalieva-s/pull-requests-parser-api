import requests
from rest_framework import serializers

from main.models import UserRequest, UserRequestResult, PullRequest


class UserRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = ('github_link', )

    def validate(self, validated_data):
        github_link = validated_data.get('github_link')
        if github_link[-1] != '/':
            github_link += '/'

        # Github links consist of at least 19 characters
        if len(github_link) <= 19:
            raise serializers.ValidationError('Given link is not a github repository link.'
                                              ' Please enter a valid repository link.')

        # In case if a given link does not start with github domain
        # or the given link is the link of the github main page
        if github_link[:18] != 'https://github.com' or github_link == 'https://github.com/':
            raise serializers.ValidationError('Given link is not a github repository link.'
                                              ' Please enter a valid repository link.')

        # Check if a given link is a link of a github user.
        # If its a user link than the link consists of one slash (not considering the domain part).
        github_user_link = github_link[20:]
        count_slashes = 0
        for i in github_user_link:
            if i == '/':
                count_slashes += 1

        if count_slashes == 1:
            raise serializers.ValidationError('You have entered a link for a github user.'
                                              ' Please enter a valid github repository link.')

        # Check if the url for a git repo really exists. For instance, a user can enter something like:
        # 'https://github.com/sehmaschine/kdflaskflas', which is not a valid repo

        r = requests.get(github_link)

        if not r:
            raise serializers.ValidationError('Given link is not a valid repository link.'
                                              ' Please enter a link for an existing repository.')

        return validated_data


class UserRequestResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRequestResult
        fields = ('github_response', 'user_request', )


class PullRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PullRequest
        fields = '__all__'
