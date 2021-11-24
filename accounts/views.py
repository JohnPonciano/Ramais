from django.shortcuts import render
from django.contrib import messages 
from django.core.validators import validate_email
# Create your views here.


def login(request):
    return render (request,'accounts/login.html')
def logout(request):
    return render (request,'accounts/logout.html')
def register(request):
 #   messages.success(request,'teste')
    if request.method != 'POST':
        messages.info(request,"Bem vindo a area de cadastro" )
        return render (request,'accounts/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if not nome or not sobrenome or not email or not username or not password or not password2:
        messages.error(request, 'Algum campo está vazio dou a informação é invalida, por gentileza preencha todo.')
        return render (request,'accounts/register.html')
    try:
        validate_email(email)
    except:
        messages.error(request, f'O email: { email } é invalido')
        return render (request,'accounts/register.html')

    return render (request,'accounts/register.html')

def dashboard(request):
    return render (request,'accounts/dashboard.html')