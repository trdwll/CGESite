# Generated by Django 2.1.7 on 2019-03-28 19:03

from django.db import migrations


class Migration(migrations.Migration):
    atomic=False
    dependencies = [
        ('blog', '0004_auto_20190328_1502'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='blog_category',
        ),
        migrations.AlterModelTable(
            name='post',
            table='blog_post',
        ),
    ]
