# Generated by Django 2.1.7 on 2019-03-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20190326_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='coupon',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
