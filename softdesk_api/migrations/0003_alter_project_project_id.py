# Generated by Django 3.2.5 on 2022-04-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_api', '0002_auto_20220403_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
