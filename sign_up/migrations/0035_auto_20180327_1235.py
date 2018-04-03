# Generated by Django 2.0.3 on 2018-03-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0034_auto_20180325_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_info',
            name='email1',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team_info',
            name='email2',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='team_info',
            name='leader_email',
            field=models.EmailField(blank=True, default=None, max_length=254, unique=True),
        ),
    ]