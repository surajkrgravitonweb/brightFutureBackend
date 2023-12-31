# Generated by Django 4.2.4 on 2023-12-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolebased', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('AccountNO', models.CharField(max_length=20)),
                ('IfscCode', models.CharField(max_length=20)),
                ('QRcodeImage', models.ImageField(upload_to='qrcodes/')),
                ('UPIid', models.CharField(max_length=255)),
                ('BankName', models.CharField(max_length=255)),
                ('mobileNumber', models.CharField(max_length=15)),
            ],
        ),
    ]
