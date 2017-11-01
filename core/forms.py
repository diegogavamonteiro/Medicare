from django import forms

from data.models import *

from django.forms import ModelForm, CharField, Textarea

# class BookForm(ModelForm):
#     class Meta:
#         model = Reserva
#         fields = ('remedio','quantity','quantity_unit','pills','doctor','crm','prescription')

# class DonationForm(ModelForm):
#     class Meta:
#         model = Donation
#         fields = ('remedio','quantity','quantity_unit','pills','date')
#
# class SupplierForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
#
#     class Meta:
#         model = Supplier
#         fields = ('full_name','razao_social','cpf','cnpj','address','description')
#         widgets = {
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.TextInput(attrs={'class': 'form-control'})
#         }
#
# class CustomerForm(ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
#
#     class Meta:
#         model = Customer
#         fields = ('full_name','mothers_name','birth_date','cpf','rg','address','sus')
#         widgets = {
#             'address': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class ContactForm(forms.Form):
    name = forms.CharField(label='NOME')
    email = forms.EmailField(label = 'E-MAIL')
    message = forms.CharField(label='MENSAGEM', widget=forms.Textarea())

class CustomerForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

    class Meta:
        model = Customer
        fields = ('full_name','mothers_name','birth_date','cpf','rg','address','sus')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

# class ReservationForm(ModelForm):
#     class Meta:
#         model = Reservation
#         fields = ('remedio','quantity','quantity_unit','pills','doctor','crm','prescription')

# class DonationForm(ModelForm):
#     class Meta:
#         model = Donation
#         fields = ('remedio','quantity','quantity_unit','pills','date')

class SupplierForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')

    class Meta:
        model = Supplier
        fields = ('full_name','razao_social','cpf','cnpj','address','description')
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }
