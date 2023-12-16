# Generated by Django 3.2.8 on 2023-12-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolebased', '0003_deposit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('social_media_facebook', models.CharField(blank=True, max_length=255)),
                ('social_media_instagram', models.CharField(blank=True, max_length=255)),
                ('social_media_linkedin', models.CharField(blank=True, max_length=255)),
                ('social_media_twitter', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('type', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
            ],
        ),
    ]
