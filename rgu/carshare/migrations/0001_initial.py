# Generated by Django 3.2.9 on 2021-12-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Pwd', models.CharField(max_length=150)),
                ('Title', models.CharField(max_length=1)),
            ],
        ),
    ]