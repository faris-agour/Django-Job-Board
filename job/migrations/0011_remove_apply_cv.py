# Generated by Django 4.2.6 on 2023-10-29 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0010_apply_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='cv',
        ),
    ]
