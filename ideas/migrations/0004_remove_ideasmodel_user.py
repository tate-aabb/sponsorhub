# Generated by Django 4.1.7 on 2023-03-15 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_ideasmodel_idea_text_alter_ideasmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideasmodel',
            name='user',
        ),
    ]