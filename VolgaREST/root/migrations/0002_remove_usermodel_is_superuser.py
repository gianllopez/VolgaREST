# Generated by Django 3.1.4 on 2021-03-15 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_superuser',
        ),
    ]