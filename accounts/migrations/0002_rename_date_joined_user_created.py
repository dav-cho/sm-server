# Generated by Django 3.2.4 on 2021-06-10 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_joined',
            new_name='created',
        ),
    ]