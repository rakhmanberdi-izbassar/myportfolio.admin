# Generated by Django 5.2.3 on 2025-06-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about_facebook_about_github_about_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
    ]
