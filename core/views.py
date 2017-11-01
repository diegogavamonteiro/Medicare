from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from .forms import CustomerForm, SupplierForm
from django.core.urlresolvers import reverse_lazy
from django.db import transaction

from data.models import Medicine

from .forms import ContactForm


User = get_user_model()

class IndexView(TemplateView):

    template_name = 'home.html'




def about(request):

    return render(request,'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Nome: {0}\nE-mail: {1}\n{2}'.format(name, email, message)
            send_mail(
            'Contato do Medicare', message, settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL]
            ) #4 parametro eh a lista de emails que deseja enviar
            success = True
    else:
        form = ContactForm()

    context = {
        'form': form,
        'success': success
    }

    return render(request,'contact.html', context)

class CustomerSignUpView(SuccessMessageMixin, FormView):
    template_name = 'customer_signup.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_signup')
    success_message = 'Cadastro realizado com sucesso!'

    def form_valid(self, form):
        customer = form.save(commit=False)
        user = User()
        user.set_password(form.data['password'])
        user.username = form.data['cpf']

        with transaction.atomic():
            user.save()
            customer.user = user
            customer.save()

        return super(CustomerSignUpView, self).form_valid(form)


def customer_signup(request):

    return render(request,'customer_signup.html')


def login(request):

    return render(request,'login.html')

def reserve(request):

    return render(request,'reserve.html')

def services(request):

    return render(request,'services.html')

def signup(request):

    return render(request,'signup.html')

class SupplierSignUpView(SuccessMessageMixin, FormView):
    template_name = 'supplier_signup.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_signup')
    success_message = 'Cadastro realizado com sucesso!'

    def form_valid(self, form):
        supplier = form.save(commit=False)
        user = User()
        user.set_password(form.data['password'])
        if form.data['cpf']:
            user.username = form.data['cpf']
        else:
            user.username = form.data['cnpj']

        with transaction.atomic():
            user.save()
            supplier.user = user
            supplier.save()

        return super(SupplierSignUpView, self).form_valid(form)

def donate(request):

    return render(request,'donate.html')

# class DonateView(SuccessMessageMixin, FormView):
#     template_name = 'donate.html'
#     form_class = DonationForm
#     success_url = reverse_lazy('donate')
#     success_message = 'Solicitação enviada com sucesso!'
#
#     def form_valid(self, form):
#         form.save(commit=True)
#         return super(DonateView, self).form_valid(form)

# class ReservationView(SuccessMessageMixin, FormView):
#     template_name = 'reserve.html'
#     form_class = ReservationForm
#     success_url = reverse_lazy('reserve')
#     success_message = 'Solicitação enviada com sucesso!'
#
#     def form_valid(self, form):
#         form.save(commit=True)
#         return super(ReservationView, self).form_valid(form)

index = IndexView.as_view()
customer_register = CustomerSignUpView.as_view()
supplier_register = SupplierSignUpView.as_view()
