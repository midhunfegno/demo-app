# Generated by Django 3.2.6 on 2021-10-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveroSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='delivereddb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferenceno', models.CharField(blank=True, max_length=100, null=True)),
                ('orderid', models.CharField(blank=True, max_length=100, null=True)),
                ('invoiceno', models.CharField(blank=True, max_length=200, null=True)),
                ('custname', models.CharField(blank=True, max_length=200, null=True)),
                ('shippingname', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('custaddress', models.CharField(blank=True, max_length=200, null=True)),
                ('pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('custmob', models.CharField(blank=True, max_length=200, null=True)),
                ('altmobno', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
