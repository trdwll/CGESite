# Generated by Django 2.2.1 on 2019-05-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20190502_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='store/products/%Y/%m/%d'),
        ),
    ]