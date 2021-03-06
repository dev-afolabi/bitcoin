# Generated by Django 3.0.3 on 2020-08-15 05:33

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(choices=[('$500', '$500'), ('$750', '$750'), ('$1000', '$1000'), ('$1,500', '$1,500'), ('$2,000', '$2,000'), ('$3,000', '$3,000'), ('$5,000', '$5,000'), ('$7,000', '$7000'), ('$10,000', '$10,000')], help_text='Select amount to deposit', max_length=25)),
                ('payment_option', models.CharField(help_text='Select payment option', max_length=25)),
                ('paid', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('10.00'))])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('payment_option', models.CharField(help_text='Select payment option', max_length=25)),
                ('account_number', models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.RegexValidator(code='invalid_characters', message='Must be numeric', regex='^[0-9]*$')])),
                ('IBAN_number', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=12, null=True)),
                ('wallet_address', models.CharField(blank=True, max_length=60, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Declined', 'Declined')], default='Pending', max_length=40, null=True)),
            ],
        ),
    ]
