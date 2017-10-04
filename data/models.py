# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid

class BaseModel(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    deleted = models.DateTimeField('Deletado em', blank=True, null=True, editable=False)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='customer')
    full_name = models.CharField('Nome Completo', max_length=200)
    mothers_name = models.CharField('Nome da Mãe', max_length=200)
    birth_date = models.DateField('Data de Nascimento')
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    address = models.TextField('Endereço')
    sus = models.CharField('Cartão do SUS', max_length=20)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

class Supplier(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='supplier', null=True)
    full_name = models.CharField('Nome Completo', max_length=200, null=True, blank=True)
    razao_social = models.CharField('Razão Social', max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    address = models.TextField('Endereço')
    description = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

UNITS = ('mg', 'g', 'kg', 'ml', 'l', 'cx')
UNIT_CHOICES = zip(UNITS, UNITS)

def prescription_file_upload(instance, filename):
    uid = uuid.uuid4()
    return 'prescriptions/%s-%s' % (uid, filename)


# class Reserva(BaseModel):
#     remedio = models.CharField('Remédio', max_length=150)
#     quantity = models.IntegerField('Quantidade', null=True)
#     quantity_unit = models.CharField('Unidade', max_length=2, choices=UNIT_CHOICES,
#                                      null=True, blank=True)
#     pills = models.IntegerField('Quantidade (em pílulas)')
#     doctor = models.CharField('Nome do Médico', max_length=150)
#     crm = models.CharField('CRM do Médico', max_length=10)
#     prescription = models.FileField('Receita', upload_to=prescription_file_upload)

class Donation(BaseModel):
    remedio = models.CharField('Remédio', max_length=150)
    quantity = models.IntegerField('Quantidade', null=True)
    quantity_unit = models.CharField('Unidade', max_length=2, choices=UNIT_CHOICES,
                                     null=True, blank=True)
    pills = models.IntegerField('Quantidade (em pílulas)')
    date = models.DateField('Data de Vencimento')

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'
        ordering = ['remedio']

    def __str__(self):
        return self.remedio
