# Generated by Django 3.2.9 on 2021-12-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshare', '0006_rename_rpass_driver_repass'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='Residence',
            field=models.CharField(default='', max_length=150),
        ),
    ]