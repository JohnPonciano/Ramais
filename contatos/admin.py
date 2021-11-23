from django.contrib import admin

# Register your models here.
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ("nome","sobrenome","telefone","categoria")
    list_display_links= ("nome","sobrenome","telefone")
    list_filter = ["categoria"]
    search_fields= ("nome","sobrenome")
    list_per_page= 10
    

admin.site.register(Categoria)
admin.site.register(Contato,ContatoAdmin)

