# Generated by Django 4.1.13 on 2023-11-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galary_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('image', models.TextField(default='')),
                ('email', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]