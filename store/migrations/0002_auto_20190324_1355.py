# Generated by Django 2.1.7 on 2019-03-24 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the category.', max_length=100)),
                ('slug', models.SlugField(help_text='The SEO slug for the category.', unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='storeitem',
            name='slug',
            field=models.SlugField(default=1, help_text='The SEO slug for the item.', unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storeitem',
            name='category',
            field=models.ForeignKey(default=1, help_text='The category that this item will be listed under.', on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
            preserve_default=False,
        ),
    ]
