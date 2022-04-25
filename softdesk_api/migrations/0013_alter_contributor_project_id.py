# Generated by Django 3.2.5 on 2022-04-24 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_api', '0012_auto_20220424_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='softdesk_api.project'),
        ),
    ]
