# Generated by Django 3.0.3 on 2020-09-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_details', '0004_message_sender_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='banktransfer',
            name='routing_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]