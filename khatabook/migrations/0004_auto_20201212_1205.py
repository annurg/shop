# Generated by Django 3.0.3 on 2020-12-12 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('khatabook', '0003_auto_20201212_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='record',
        ),
        migrations.RemoveField(
            model_name='record',
            name='bill',
        ),
        migrations.AddField(
            model_name='items',
            name='record',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='khatabook.Record'),
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='khatabook.Person'),
        ),
    ]
