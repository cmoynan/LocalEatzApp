# Generated by Django 4.2.14 on 2024-07-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactquery',
            name='message',
        ),
        migrations.AddField(
            model_name='contactquery',
            name='phone_number',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]
