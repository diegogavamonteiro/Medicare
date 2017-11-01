# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import uuid


UNITS = ('mg', 'g', 'kg', 'ml', 'l', 'cx')
UNIT_CHOICES = zip(UNITS, UNITS)


def prescription_file_upload(instance, filename):
    uid = uuid.uuid4()
    return 'prescriptions/%s-%s' % (uid, filename)


class BaseModel(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    deleted = models.DateTimeField('Deletado em', blank=True, null=True, editable=False)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        abstract = True

class Medicine(BaseModel):
    active_principle = models.CharField('Princípio Ativo',max_length=150)
    remedio = models.CharField('Remédio',max_length=150)
    tarja = models.CharField('Tarja', max_length=20, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['remedio']

    def __str__(self):
        return str(self.id)

class Medicine_Apresentation(BaseModel):
    id_medicine = models.ForeignKey('data.Medicine',on_delete=models.CASCADE, verbose_name='Id Medicamento')
    ggrem = models.CharField('Código Regulação Econômica', max_length=15,null=True)
    size = models.IntegerField('Tamanho', null=True)
    size_unit = models.CharField('Unidade', max_length=2, choices=UNIT_CHOICES,
                                     null=True, blank=True)
    laboratory = models.CharField('Laboratório', max_length=200, null=True)
    complement = models.TextField('Complemento', blank=True)

    class Meta:
        verbose_name = 'Apresentação de Medicamento'
        verbose_name_plural = 'Apresentação de Medicamentos'
        ordering = ['id_medicine']

    def __str__(self):
        return str(self.id)

class Doctor(BaseModel):
    full_name = models.CharField('Nome Completo', max_length=200)
    crm = models.CharField('CRM do Médico', max_length=10)
    state = models.CharField('Estado', max_length=2)

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
        ordering = ['full_name']

    def __str__(self):
        return str(self.id)

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
    email = models.TextField('E-mail', default='Atualizar')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['full_name']

    def __str__(self):
        return str(self.id)

class Supplier(BaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='supplier', null=True)
    full_name = models.CharField('Nome Completo', max_length=200, null=True, blank=True)
    razao_social = models.CharField('Razão Social', max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True)
    address = models.TextField('Endereço')
    description = models.TextField('Descrição', blank=True)
    email = models.TextField('E-mail', default='Atualizar')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['full_name']

    def __str__(self):
        return str(self.id)


class Reservation(BaseModel):

    prescription = models.FileField('Prescrição Médica', upload_to=prescription_file_upload)
    date = models.DateField('Data de Vencimento do Remédio')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Reservation_Itens(BaseModel):
    id_reservation = models.ForeignKey('data.Reservation',on_delete=models.CASCADE)
    id_customer = models.ForeignKey('data.Customer',on_delete=models.CASCADE)
    id_doctor = models.ForeignKey('data.Doctor',on_delete=models.CASCADE)
    id_apresentation = models.ForeignKey('data.Medicine_Apresentation',on_delete=models.CASCADE)

    pills = models.IntegerField('Quantidade (em pílulas)')

    class Meta:
        verbose_name = 'Itens de Reserva'
        verbose_name_plural = 'Itens de Reservas'
        ordering = ['id_reservation']

    def __str__(self):
        return str(self.id)


class Donation(BaseModel):
    date = models.DateField('Data de Vencimento do Remédio')

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Donation_Itens(BaseModel):
    id_donation = models.ForeignKey('data.Donation',on_delete=models.CASCADE)
    id_supplier = models.ForeignKey('data.Supplier',on_delete=models.CASCADE)
    id_apresentation = models.ForeignKey('data.Medicine_Apresentation',on_delete=models.CASCADE)

    pills = models.IntegerField('Quantidade (em pílulas)')

    class Meta:
        verbose_name = 'Itens de Doação'
        verbose_name_plural = 'Itens de Doações'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Stock(BaseModel):
    id_reservation_itens = models.ForeignKey('data.Reservation_Itens',on_delete=models.CASCADE,blank=True,null=True)
    id_donation_itens = models.ForeignKey('data.Donation_Itens',on_delete=models.CASCADE,blank=True,null=True)
    stock_quantity = models.IntegerField('Quantidade em Estoque')
    minimun_quantity = models.IntegerField('Quantidade Mínima')

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoque'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Stock_Itens(BaseModel):
    id_stock = models.ForeignKey('data.Stock',on_delete=models.CASCADE)
    manufacture_date = models.DateField('Data de Fabricação',null=True)
    due_date = models.DateField('Data de Vencimento')
    quantity = models.IntegerField('Quantidade', default=0)

    class Meta:
        verbose_name = 'Itens de Estoque'
        verbose_name_plural = 'Itens de Estoque'
        ordering = ['id']

    def __str__(self):
        return str(self.id)
