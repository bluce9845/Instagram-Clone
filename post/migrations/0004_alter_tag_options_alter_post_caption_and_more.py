# Generated by Django 5.1.1 on 2024-10-15 06:54

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_tag_options_alter_post_caption_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=10000, verbose_name='Caption'),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stream',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stream_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='stream',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]