# Generated by Django 4.0.2 on 2022-02-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0003_alter_usertable_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertable',
            name='user_id',
            field=models.PositiveBigIntegerField(null=True, unique=True),
        ),
    ]
