# Generated by Django 3.0.3 on 2020-05-14 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200514_0604'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PointProducts',
            new_name='PointProduct',
        ),
    ]