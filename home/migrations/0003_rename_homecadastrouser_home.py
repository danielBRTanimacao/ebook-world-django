# Generated by Django 5.0.3 on 2024-03-18 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homecadastrouser_delete_home'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeCadastroUser',
            new_name='Home',
        ),
    ]
