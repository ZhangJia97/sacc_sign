# Generated by Django 2.0.3 on 2018-03-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0011_actor_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor_info',
            name='owner',
        ),
        migrations.AddField(
            model_name='team_info',
            name='is_added',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Actor_info',
        ),
    ]
