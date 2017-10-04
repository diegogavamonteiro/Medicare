from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request,'home.html')

def about(request):

    return render(request,'about.html')

def contact(request):

    return render(request,'contact.html')

def customerSignup(request):

    return render(request,'customer_signup.html')

def donate(request):

    return render(request,'donate.html')

def login(request):

    return render(request,'login.html')

def reserve(request):

    return render(request,'reserve.html')

def services(request):

    return render(request,'services.html')

def signup(request):

    return render(request,'signup.html')

def supplier_signup(request):

    return render(request,'supplier_signup.html')
