# Generated by Django 2.0.3 on 2018-03-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0023_auto_20180322_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=100)),
                ('is_added', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='team_info',
            name='is_added',
        ),
    ]
