# Generated by Django 3.0.2 on 2020-04-12 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_merge_20200310_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='resource_type',
        ),
    ]
