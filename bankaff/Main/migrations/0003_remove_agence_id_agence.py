# Generated by Django 3.2.8 on 2021-10-09 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_agence_id_agence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agence',
            name='id_agence',
        ),
    ]
