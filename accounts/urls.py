from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.user_login, name='login'),
    path('tela-cadastro/',views.tela_cadastro, name='tela-cadastro')
]
