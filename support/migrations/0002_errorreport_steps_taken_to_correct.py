# Generated by Django 4.2.11 on 2024-05-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorreport',
            name='steps_taken_to_correct',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
