# Generated by Django 5.0.3 on 2024-03-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_homecadastrouser_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='all_books',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='home',
            name='all_pages',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
