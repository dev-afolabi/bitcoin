# Generated by Django 3.0.3 on 2020-08-11 20:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0003_deposit_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='IBAN_number',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='account_number',
            field=models.CharField(default=65456, max_length=25, validators=[django.core.validators.RegexValidator(code='invalid_characters', message='Must be numeric', regex='^[0-9]*$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='bank_name',
            field=models.CharField(default='testing', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='payment_option',
            field=models.CharField(default='testing', help_text='Select payment option', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'Successful'), ('Declined', 'Declined')], default='Pending', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='swift_code',
            field=models.CharField(default='testing', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='withdrawal',
            name='wallet_address',
            field=models.CharField(default='tetsing', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]