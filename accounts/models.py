from django.db import models
from contatos.models import Contato
from django import forms
# Create your models here.



class FormConato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ()