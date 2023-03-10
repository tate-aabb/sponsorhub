# Generated by Django 4.1.7 on 2023-03-02 15:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0002_alter_ideasmodel_idea_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideasmodel',
            name='Idea_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ideasmodel',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
