# Generated by Django 5.1 on 2024-08-15 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0010_alter_link_dislikes_alter_link_likes_alter_link_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='link',
            name='likes',
        ),
    ]
