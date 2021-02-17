# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-17 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_date', models.DateTimeField()),
                ('app_hour', models.CharField(choices=[('10:00am - 11:00am', '10:00am - 11:00am'), ('11:00am - 12:00pm', '11:00am - 12:00pm'), ('2:00pm - 3:00pm', '2:00pm - 3:00pm'), ('3:00pm - 4:00pm', '3:00pm - 4:00pm')], default='10:00am - 11:00am', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('details', models.CharField(max_length=600)),
                ('doctor_image', models.ImageField(upload_to='images/')),
                ('departments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='hospitals',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Patient'),
        ),
    ]
