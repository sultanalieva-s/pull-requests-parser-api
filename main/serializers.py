from rest_framework import serializers

from main.models import UserRequest, UserRequestResult, PullRequest


class UserRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = ('github_link', )

    def validate(self, validated_data):
        github_link = validated_data.get('github_link')

        # TODO: github link validation

        # if not github_link:
        #     raise serializers.ValidationError('Given link is not a github link. Please enter a valid github link.')

        return validated_data


class UserRequestResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRequestResult
        fields = ('github_response', 'user_request', )


class PullRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PullRequest
        fields = '__all__'

