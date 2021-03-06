# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-03 19:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('deleted', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deletado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('full_name', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('mothers_name', models.CharField(max_length=200, verbose_name='Nome da Mãe')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=10)),
                ('address', models.TextField(verbose_name='Endereço')),
                ('sus', models.CharField(max_length=20, verbose_name='Cartão do SUS')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('deleted', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deletado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('remedio', models.CharField(max_length=150, verbose_name='Remédio')),
                ('quantity', models.IntegerField(null=True, verbose_name='Quantidade')),
                ('quantity_unit', models.CharField(blank=True, choices=[('mg', 'mg'), ('g', 'g'), ('kg', 'kg'), ('ml', 'ml'), ('l', 'l'), ('cx', 'cx')], max_length=2, null=True, verbose_name='Unidade')),
                ('pills', models.IntegerField(verbose_name='Quantidade (em pílulas)')),
                ('date', models.DateField(verbose_name='Data de Vencimento')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('deleted', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deletado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nome Completo')),
                ('razao_social', models.CharField(blank=True, max_length=200, null=True, verbose_name='Razão Social')),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True)),
                ('address', models.TextField(verbose_name='Endereço')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['full_name'],
            },
        ),
    ]
