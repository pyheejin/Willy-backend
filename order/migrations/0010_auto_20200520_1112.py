# Generated by Django 3.0.6 on 2020-05-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='anonymous',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
