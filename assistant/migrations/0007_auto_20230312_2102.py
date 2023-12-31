# Generated by Django 3.2.18 on 2023-03-12 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assistant', '0006_auto_20221012_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tokentoresetpassword',
            name='user',
        ),
        migrations.CreateModel(
            name='ResetPasswordRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant.tokentoresetpassword')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
