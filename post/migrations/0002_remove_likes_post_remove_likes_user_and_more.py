# Generated by Django 5.1.1 on 2024-10-10 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='post',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='following',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='post',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]
