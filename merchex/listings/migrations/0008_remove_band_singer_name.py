# Generated by Django 5.0.6 on 2024-05-16 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_singer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='singer_name',
        ),
    ]