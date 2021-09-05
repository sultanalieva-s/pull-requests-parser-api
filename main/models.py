from django.db import models
# Create your models here.


class UserRequest(models.Model):
    github_link = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'ID: ' + str(self.id) + '. Link: ' + self.github_link


class UserRequestResult(models.Model):
    user_request = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    github_response = models.TextField()

    def __str__(self):
        return 'Response: ' + self.github_response + '. User Request id: ' + str(self.user_request)


class PullRequest(models.Model):
    user_request = models.ForeignKey(UserRequest, on_delete=models.CASCADE, related_name='pull_requests')
    user_request_result = models.ForeignKey(UserRequestResult, on_delete=models.CASCADE, related_name='pull_requests')

    pull_request_title = models.CharField(max_length=255)
    pull_request_link = models.CharField(max_length=255)
    assignees = models.TextField(null=True, blank=True)
    reviewers = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.pull_request_title
