# Generated by Django 3.2.12 on 2022-05-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=250)),
                ('movie_link', models.CharField(max_length=250)),
                ('movie_year', models.IntegerField()),
                ('movie_nomination', models.IntegerField()),
            ],
        ),
    ]
