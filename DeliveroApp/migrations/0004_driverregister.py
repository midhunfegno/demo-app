# Generated by Django 3.2.6 on 2021-09-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveroApp', '0003_rename_name_adminregister_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='driverregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=100, null=True)),
                ('lname', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=40, null=True)),
                ('mobno', models.CharField(blank=True, max_length=20, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
