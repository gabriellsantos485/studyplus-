# url - view - template

from django.urls import path, include
from .views import HomeFilmes, HomePage, DetalhesFilmes, LogicaProgramacao

urlpatterns =[
    path('', HomePage.as_view()),
    path('aulas/', HomeFilmes.as_view()),
    path('aulas/<int:pk>', DetalhesFilmes.as_view()),
    path('programacao/', LogicaProgramacao.as_view())
]