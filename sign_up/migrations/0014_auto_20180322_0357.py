# Generated by Django 2.0.3 on 2018-03-22 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0013_team_info_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team_info',
            old_name='key',
            new_name='team_key',
        ),
    ]
