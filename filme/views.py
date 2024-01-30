from django.shortcuts import render
from .models import Filme, LISTA_CATEGORIAS
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def categoria(request):
    categorias = LISTA_CATEGORIAS #funçao habilitada, usar para criar tela de categorias
    return render(request, "homecategorias.html",{'categorias':categorias})

class HomePage(TemplateView):
    template_name = "homepage.html"

class HomeFilmes(ListView):
    template_name =  'homecategorias.html'
    model = Filme
    # object.list

class DetalhesFilmes(DetailView):
    template_name = "detalhefilme.html"
    model = Filme

class LogicaProgramacao(TemplateView):
    template_name = "logicadeprogramacao.html"
