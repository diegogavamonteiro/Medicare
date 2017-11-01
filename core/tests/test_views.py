# coding=utf-8

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail
from django.contrib.auth import get_user_model
from django.conf import settings

from model_mommy import mommy

User = get_user_model()

class IndexViewTextCase(TestCase):

    def setUp(self): # criar alguma coisa para cada teste
        self.cliente = Client()
        self.url = reverse('home')

    def tearDown(self): # remover alguma coisa para cada teste
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200) # http 200 = OK / http 404 = Nao encontrado / http 302 = Redirect ( Movido Temporariamente ) / http 500 = Erro de servidor

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'home.html')

class ContactViewTestCase(TestCase):

    def setUp(self): # criar alguma coisa para cada teste
        self.cliente = Client()
        self.url = reverse('contact')

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_error(self):
        data = {'name': '', 'message': '', 'email': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.')

    def test_form_ok(self):
        data = {'name': 'test', 'message': 'test', 'email': 'test@test.com'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato do Medicare')

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        data = {'username': self.user.username, 'password': '123'}
        response = self.client.post(self.login_url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url, status_code=302)
        self.assertTrue(response.wsgi_request.user.is_authenticated()) # usuário logado

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.login_url,data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        error_msg = ('Por favor, entre com um usuário  e senha corretos.'
        ' Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(response, 'form', None, error_msg)

class RegisterCustomerViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('customer_signup')

    # def test_register_ok(self):
    #     data = {'username': 'gileno', 'password1': 'teste123', 'password2': 'teste123'}
    #     response = self.client.post(self.register_url, data)
    #     index_url = reverse('home')
    #     self.assertRedirects(response, index_url)
    #     self.assertEquals(User.objects.count(), 1)
