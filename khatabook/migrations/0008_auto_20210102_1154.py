# Generated by Django 3.0.3 on 2021-01-02 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khatabook', '0007_auto_20201225_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
