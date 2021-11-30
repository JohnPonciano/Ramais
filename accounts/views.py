from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):

    if request.method != 'POST':
        return render(request,'accounts/login.html')
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=username , password=password )

    
    if not user:
        messages.error(request, "Usuario ou senha invalido")
        return render (request,'accounts/login.html')
    else:
        auth.login(request,user)
        messages.success(request, "Boa !")
        #return render (request,'')
        return redirect("dashboard")
        

def logout(request):
    return render (request,'accounts/logout.html')

def register(request):

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
    if len(password) < 6 or password != password2:
        messages.error(request,'Senha muito curta, ou nao sao iguais')
        return render(request,'accounts/register.html')

    if User.objects.filter(username=username).exists() or len(username) < 3 :
        messages.error(request,'Usuario ja exite ou nome muito curto')
        return render (request,'accounts/register.html')

    if User.objects.filter(email = email).exists():
        messages.error(request, 'O email ja foi usado')
        return render (request,'accounts/register.html')
    
    messages.success(request, 'Usuario registrado :) agora e so fazer login!! ')
    user = User.objects.create_user(username=username,email=email,password=password, 
                                                    first_name=nome, last_name=sobrenome)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    return render (request,'accounts/dashboard.html')