# Generated by Django 3.2.6 on 2021-09-15 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveroApp', '0004_driverregister'),
    ]

    operations = [
        migrations.CreateModel(
            name='taskdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(blank=True, max_length=100, null=True)),
                ('created_date', models.CharField(default='0', max_length=20)),
                ('Orderid', models.CharField(blank=True, max_length=100, null=True)),
                ('Invoiceno', models.CharField(blank=True, max_length=100, null=True)),
                ('Productcode', models.CharField(blank=True, max_length=100, null=True)),
                ('Drivercode', models.CharField(blank=True, max_length=100, null=True)),
                ('Custmob', models.CharField(blank=True, max_length=100, null=True)),
                ('Custname', models.CharField(blank=True, max_length=100, null=True)),
                ('Shippingname', models.CharField(blank=True, max_length=100, null=True)),
                ('District', models.CharField(blank=True, max_length=100, null=True)),
                ('Custaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('Pincode', models.CharField(blank=True, max_length=100, null=True)),
                ('Altmobno', models.CharField(blank=True, max_length=100, null=True)),
                ('Preferenceno', models.CharField(blank=True, max_length=100, null=True)),
                ('Lattitude', models.CharField(blank=True, max_length=100, null=True)),
                ('Longitude', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
