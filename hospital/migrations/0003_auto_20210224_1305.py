# Generated by Django 3.1.7 on 2021-02-24 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20210224_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor'),
        ),
    ]