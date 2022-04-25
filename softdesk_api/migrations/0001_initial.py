# Generated by Django 3.2.5 on 2022-04-03 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
                ('role', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=1000)),
                ('tag', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('project_id', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('author_user_id', models.IntegerField()),
                ('assignee_user_id', models.IntegerField()),
                ('created_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('type', models.CharField(max_length=100)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('created_time', models.DateField()),
                ('author_use_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('issue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue_related', to='softdesk_api.issue')),
            ],
        ),
    ]
