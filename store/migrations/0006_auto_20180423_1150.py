# Generated by Django 2.0.4 on 2018-04-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20180423_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='images/placeholder.jpg', upload_to='images'),
        ),
    ]
