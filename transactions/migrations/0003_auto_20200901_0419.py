# Generated by Django 3.0.3 on 2020-09-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20200814_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='paid',
        ),
        migrations.AddField(
            model_name='deposit',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Successful', 'confirmed')], default='Pending', max_length=40, null=True),
        ),
    ]
