# Generated by Django 3.0.4 on 2020-03-30 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200329_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='controllogin',
            name='city',
            field=models.CharField(default='OI', max_length=255, verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='controllogin',
            name='phone_number',
            field=models.CharField(default='3100000', max_length=11, verbose_name='Whatsapp'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='controllogin',
            name='uf',
            field=models.CharField(default='MG', max_length=2, verbose_name='Estado'),
            preserve_default=False,
        ),
    ]
