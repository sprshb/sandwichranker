# Generated by Django 3.2.16 on 2023-01-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sandwich_id', models.CharField(max_length=255, unique=True)),
                ('average_rating', models.FloatField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('total_submissions', models.IntegerField(default=0)),
            ],
        ),
    ]
