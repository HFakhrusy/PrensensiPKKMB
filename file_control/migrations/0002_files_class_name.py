# Generated by Django 3.2.13 on 2022-08-13 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0016_auto_20220814_0022'),
        ('file_control', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='class_name',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='presence.classname'),
        ),
    ]
