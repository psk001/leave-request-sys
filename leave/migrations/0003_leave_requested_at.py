# Generated by Django 4.0.4 on 2022-05-24 16:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_alter_leave_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='requested_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
