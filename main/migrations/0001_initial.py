# Generated by Django 3.2 on 2021-09-05 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_link', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRequestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_response', models.TextField()),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.userrequest')),
            ],
        ),
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pull_request_title', models.CharField(max_length=255)),
                ('pull_request_link', models.CharField(max_length=255)),
                ('assignees', models.TextField()),
                ('reviewers', models.TextField()),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pull_requests', to='main.userrequest')),
                ('user_request_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pull_requests', to='main.userrequestresult')),
            ],
        ),
    ]
