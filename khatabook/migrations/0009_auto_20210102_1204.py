# Generated by Django 3.0.3 on 2021-01-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khatabook', '0008_auto_20210102_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='total_amount',
            field=models.DecimalField(decimal_places=1, editable=False, max_digits=10, null=True),
        ),
    ]
