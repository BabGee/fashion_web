# Generated by Django 3.1 on 2020-08-07 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200807_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='fashion.jpg', upload_to='product_pics'),
        ),
    ]
