from django.db import models
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Contato
from django.core.paginator import Paginator
from django.db.models import Q,Value,F
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.



def index(request):
    contatos = Contato.objects.order_by('categoria').filter(mostrar=True)
    paginator = Paginator(contatos,10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request,'contatos/index.html',{
        'contatos': contatos
    })

def show_contato(request, contato_id):
    #  contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request,'contatos/show_contato.html',{
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')


    # message about erros
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR,
        'Ocorreu um erro, esse campo não pode estar vazio')
        return redirect('index')

    campos = Concat('nome', Value(' '),'sobrenome')


    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains= termo) |
        Q(telefone__icontains= termo)| 
        Q(categoria__nome__icontains= termo)
    )

    print(contatos.query)
    return render(request,'contatos/busca.html',{
        'contatos': contatos

    })
