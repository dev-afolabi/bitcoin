# Generated by Django 3.0.3 on 2020-08-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20200809_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
