# Generated by Django 3.0.4 on 2020-03-30 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controllogin',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]