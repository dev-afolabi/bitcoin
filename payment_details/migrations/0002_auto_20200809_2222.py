# Generated by Django 3.0.3 on 2020-08-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banktransfer',
            name='account_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='banktransfer',
            name='bank_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='banktransfer',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='btctransfer',
            name='btc_address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='btctransfer',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
