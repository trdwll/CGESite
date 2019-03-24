# Generated by Django 2.1.7 on 2019-03-24 18:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic=False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_auto_20190324_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.StoreItem')),
            ],
            options={
                'db_table': 'store_item_rating',
            },
        ),
        migrations.AlterModelTable(
            name='category',
            table='store_category',
        ),
        migrations.AlterModelTable(
            name='coupon',
            table='store_coupon',
        ),
    ]
