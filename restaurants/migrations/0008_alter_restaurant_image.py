# Generated by Django 4.2.14 on 2024-07-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='restaurant_images/'),
        ),
    ]
