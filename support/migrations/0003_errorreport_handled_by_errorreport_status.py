# Generated by Django 4.2.11 on 2024-05-31 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_errorreport_steps_taken_to_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='errorreport',
            name='handled_by',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_superuser': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='errorreport',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')], default='open', max_length=20),
        ),
    ]
