# Generated by Django 3.1 on 2021-01-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_auto_20210110_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='Current_Balance',
            field=models.IntegerField(max_length=1000000000),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='Amount',
            field=models.IntegerField(max_length=1000000000),
        ),
    ]
