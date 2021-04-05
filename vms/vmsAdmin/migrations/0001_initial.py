# Generated by Django 3.1.7 on 2021-04-04 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcl_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Vehicle Name')),
                ('vcl_number', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Vehicle ID')),
                ('vcl_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Vehicle Category')),
                ('costperkm', models.IntegerField(blank=True, null=True, verbose_name='Cost per km')),
                ('costperhr', models.IntegerField(blank=True, null=True, verbose_name='Cost per hour')),
                ('mileage', models.IntegerField(blank=True, null=True, verbose_name='Mileage')),
                ('vcl_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drvr_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Driver ID')),
                ('drvr_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Driver Name')),
                ('drvr_contact_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='Driver Contact Number')),
                ('drvr_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Driver Email Address')),
                ('drvr_vcl', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vmsAdmin.vehicles')),
            ],
        ),
    ]
