# Generated by Django 4.2.14 on 2024-07-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='email',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_images/'),
        ),
    ]
