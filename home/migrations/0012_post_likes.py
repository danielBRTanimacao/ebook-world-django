# Generated by Django 5.0.3 on 2024-05-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
