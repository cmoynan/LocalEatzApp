# Generated by Django 4.2.14 on 2024-07-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurant_max_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='max_tables',
            field=models.IntegerField(default=3),
        ),
    ]
