# Generated by Django 4.0.5 on 2022-06-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_rename_effective_data_event_effective_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]