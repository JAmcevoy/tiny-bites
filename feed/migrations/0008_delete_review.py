# Generated by Django 4.2.11 on 2024-05-07 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_create_featured_image_review_featured_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]