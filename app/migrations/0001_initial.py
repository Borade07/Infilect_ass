# Generated by Django 3.2.9 on 2023-02-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=255)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]