# Generated by Django 3.0.3 on 2020-12-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khatabook', '0002_auto_20201212_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='record',
        ),
        migrations.AddField(
            model_name='person',
            name='record',
            field=models.ManyToManyField(to='khatabook.Record'),
        ),
    ]
