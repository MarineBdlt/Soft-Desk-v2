# Generated by Django 3.2.5 on 2022-04-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_api', '0013_alter_contributor_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project_id',
            field=models.IntegerField(),
        ),
    ]
