# Generated by Django 4.0.2 on 2022-02-09 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertable',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usertable',
            name='username',
        ),
    ]
