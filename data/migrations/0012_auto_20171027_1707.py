# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20171027_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_itens',
            name='id_medicine',
        ),
        migrations.AlterField(
            model_name='medicine_apresentation',
            name='ggrem',
            field=models.CharField(max_length=15, null=True, verbose_name='Código Regulação Econômica'),
        ),
        migrations.AlterField(
            model_name='medicine_apresentation',
            name='laboratory',
            field=models.CharField(max_length=200, null=True, verbose_name='Laboratório'),
        ),
    ]
