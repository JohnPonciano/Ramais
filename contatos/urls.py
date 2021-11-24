from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('<int:contato_id>', views.show_contato, name='show_contato'),
    path('busca/',views.busca,name='busca')
]