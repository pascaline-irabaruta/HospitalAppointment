# Generated by Django 3.1.7 on 2021-02-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_image',
            field=models.ImageField(blank=True, upload_to='doctors/'),
        ),
    ]
