# Generated by Django 3.0.9 on 2023-04-07 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20230407_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='launch_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
