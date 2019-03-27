# Generated by Django 2.1.7 on 2019-03-26 21:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_auto_20190324_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'store_item_review',
            },
        ),
        migrations.AddField(
            model_name='storeitem',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userreview',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.StoreItem'),
        ),
    ]
