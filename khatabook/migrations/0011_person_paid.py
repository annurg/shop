# Generated by Django 3.0.3 on 2021-01-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khatabook', '0010_auto_20210102_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='paid',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
