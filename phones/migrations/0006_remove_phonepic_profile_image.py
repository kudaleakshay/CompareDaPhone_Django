# Generated by Django 2.0 on 2017-12-29 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_auto_20171229_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonepic',
            name='profile_image',
        ),
    ]