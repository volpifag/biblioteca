from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request):
        pass


class LivrosView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

    # def post(self, request, *args, **kwargs):
    # Aqui você pode adicionar a lógica do POST, se necessário.


class EmprestimoView(View):
    def get(self, request, *args, **kwargs):
        reservas = Emprestimo.object 
        return render(request, 'reserva.html', {'reservas': reservas})
#nao tem emprestimo

class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})


class AutoresView(View):
    def get(self, request, *args, **kwargs):
        autores = Autor.objects.all()
        return render(request, 'autor.html', {'autores': autores})


class EditorasView(View):
    def get(self, request, *args, **kwargs):
        editoras = Editora.objects.all()
        return render(request, 'editora.html', {'editoras': editoras})


class LeitoresView(View):
    def get(self, request, *args, **kwargs):
        leitores = Leitor.objects.all()
        return render(request, 'leitor.html', {'leitores': leitores})


class GenerosView(View):
    def get(self, request, *args, **kwargs):
        generos = Genero.objects.all()
        return render(request, 'genero.html', {'generos': generos})
from django.shortcuts import redirect
from django.contrib import messages
from django.views import View
from .models import Livro

class DeleteLivroView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            livro = Livro.objects.get(id=id)
            livro.delete()
            messages.success(request, 'Livro excluído com sucesso!')  # Success message
        except Livro.DoesNotExist:
            messages.error(request, 'Livro não encontrado.')  # Error message if Livro doesn't exist
        return redirect('livros')
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
path('admin/', admin.site.urls),
path('', ConsultaView.as_view(), name='livros'),
path('reserva/', ReservaView.as_view(),
name='reserva'),
path('delete/<int:id>/', DeleteLivroView.as_view(),
name='delete'),]