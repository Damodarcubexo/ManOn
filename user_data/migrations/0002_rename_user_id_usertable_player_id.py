# Generated by Django 4.0.2 on 2022-02-14 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertable',
            old_name='user_id',
            new_name='player_id',
        ),
    ]
