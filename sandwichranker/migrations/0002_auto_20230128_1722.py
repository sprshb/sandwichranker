# Generated by Django 3.2.16 on 2023-01-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sandwichranker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandwich',
            name='sandwich_image',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='sandwich',
            name='sandwich_name',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
