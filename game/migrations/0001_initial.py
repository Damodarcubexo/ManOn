# Generated by Django 3.2.12 on 2022-03-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1', models.CharField(max_length=50)),
                ('player1_score', models.IntegerField(default=0)),
                ('player2', models.CharField(max_length=50)),
                ('player2_score', models.IntegerField(default=0)),
                ('dateTime', models.DateTimeField()),
                ('player1_team', models.CharField(max_length=50)),
                ('player2_team', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid1', models.IntegerField()),
                ('userid2', models.IntegerField()),
                ('player1', models.CharField(max_length=100)),
                ('player2', models.CharField(max_length=100)),
                ('team1', models.CharField(max_length=100)),
                ('team2', models.CharField(max_length=100)),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('positions1', models.BooleanField()),
                ('position2', models.BooleanField()),
                ('inning', models.IntegerField()),
                ('balls', models.IntegerField()),
                ('outs', models.IntegerField()),
                ('donehits', models.IntegerField()),
                ('EH', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('player_id', models.IntegerField()),
                ('player_name', models.CharField(max_length=50)),
                ('player_team', models.CharField(max_length=50)),
            ],
        ),
    ]
