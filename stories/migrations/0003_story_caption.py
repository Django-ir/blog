# Generated by Django 4.1.3 on 2022-12-04 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
