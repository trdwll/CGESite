# Generated by Django 2.2 on 2019-05-01 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20190501_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forum.Topic'),
            preserve_default=False,
        ),
    ]