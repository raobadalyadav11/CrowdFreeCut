# Generated by Django 4.2 on 2023-05-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0003_alter_salonservice_salon'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='salon/thumbnail'),
        ),
    ]