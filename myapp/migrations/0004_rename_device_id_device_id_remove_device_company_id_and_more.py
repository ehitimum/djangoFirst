# Generated by Django 4.2 on 2023-04-09 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_company_id_company_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_id',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='device',
            name='company_id',
        ),
        migrations.AddField(
            model_name='device',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.company'),
        ),
    ]
