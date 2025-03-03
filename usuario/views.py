from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from usuario.forms import *




def inicio(request):
    return render(
        request=request,
        template_name='usuario/inicio.html',
    )


def ayuda(request):
    return render(
        request=request,
        template_name='usuario/ayuda.html',
    )


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            messages.success(request, "Usuario creado correctamente")
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='usuario/registro.html',
        context={'form': formulario},
    )

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                messages.success(request, "Se ha iniciado Sesión")
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='usuario/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
    template_name = 'usuario/logout.html'



#EDITAR USUARIO
class ProfileUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
        model = User
        form_class = UserUpdateForm
        success_message = "%(calculated_field)s  was created successfully"
        success_url = reverse_lazy('inicio')
        template_name = 'usuario/editar_perfil.html'
        def get_object(self, queryset=None):
            return self.request.user
        
        


#AVATAR
@login_required
def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES) # Aquí me llega toda la info del formulario html

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            messages.success(request, "Avatar agregado correctamente")
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='usuario/formulario_avatar.html',
        context={'form': formulario},
    )






