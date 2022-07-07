# Generated by Django 4.0.2 on 2022-02-28 05:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning_logs', '0003_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 13, 14, 18, 506749)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 13, 14, 18, 506749)),
        ),
    ]