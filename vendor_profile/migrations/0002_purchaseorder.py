# Generated by Django 5.0.4 on 2024-04-09 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=50, unique=True, verbose_name='Purchase Order')),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('delivery_date', models.DateTimeField(auto_now=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('quality_rating', models.FloatField()),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('acknowledgment_date', models.DateTimeField(auto_now=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor_profile.employeeinformation', verbose_name='Vendor Code')),
            ],
        ),
    ]