from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import *
# from .forms import *


########## VIEWS PRINCIPALES #############

def home(request):
    return render(request,"home.html")



def about(request):
    return render(request, "about.html")



# def pages(request):
#     publicaciones = Blog.objects.all()
#     return render(request, "pages.html", {"publicaciones" : publicaciones})

##########################################

######### VIEWS DE PUBLICACIONES #########

# def get_page(request, id):
#     publicacion = Blog.objects.filter(id=id)
#     if publicacion is not None:
#         return render(request, "get_page.html", {"publicacion" : publicacion})
#     else:
#         return render(request, "get_page.html", {"mensaje" : "No hay páginas aún"})



# @login_required
# def crear_page(request):
#     if request.method == "POST":
#         formulario = BlogForm(request.POST)
#         if formulario.is_valid():
#             info = formulario.cleaned_data
#             titulo = info["titulo"]
#             subtitulo = info["subtitulo"]
#             cuerpo = info["cuerpo"]
#             autor = info["autor"]
#             fecha = info["fecha"]
#             imagen = info["imagen"]
#             blog = Blog(titulo = titulo, subtitulo = subtitulo, cuerpo = cuerpo, autor = autor, fecha = fecha, imagen = imagen)
#             blog.save()
#             return render(request, "pages.html", {"mensaje" : "publicación creada correctamente"})
#         else:
#             return render(request, "crear_page.html", {"mensaje" : "Datos inválidos, vuelva a intentarlo", "formulario" : BlogForm()})

#     else:
#         return render(request, "crear_page.html", {"formulario" : BlogForm()})



# @login_required
# def editar_page(request, id):
#     publicacion = Blog.objects.get(id=id)
#     formulario_viejo = BlogForm(instance = publicacion)
#     if request.method == "POST":
#         formulario_nuevo = BlogForm(request.POST)
#         if formulario_nuevo.is_valid():
#             info = formulario_nuevo.cleaned_data
#             publicacion.titulo = info["titulo"]
#             publicacion.subtitulo = info["subtitulo"]
#             publicacion.cuerpo = info["cuerpo"]
#             publicacion.autor = info["autor"]
#             publicacion.fecha = info["fecha"]
#             publicacion.imagen = info["imagen"]
#             publicacion.save()
#             return render(request, "get_page.html", {"mensaje" : "Publicación editada correctamente", "publicacion" : publicacion})
#         else:
#             return render(request, "editar_page.html", {"formulario" : formulario_viejo, "mensaje" : "Datos inválidos, vuelva a intentarlo"})

#     else:
#         return render(request, "editar_page.html", {"formulario" : formulario_viejo})



# @login_required
# def eliminar_page(request, id):
#     publicacion = Blog.objects.get(id=id)
#     publicacion.delete()
#     return render(request, "pages.html", {"mensaje" : "Publicacion eliminada correctamente"})

##########################################

########### VIEWS DEL USUARIO ############

def get_perfil(request):
    usuario = request.user
    return render(request, "get_perfil.html", {"usuario" : usuario})



def login(request):
    fallo = render(request, "login.html", {"mensaje" : "Usuario o contraseña incorrectos", "formulario" : AuthenticationForm()})

    if request.method == "POST":
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid():
            nombre = request.POST["username"]
            contraseña = request.POST["password"]
            user = authenticate(username = nombre, password = contraseña)
            if user is not None:
                login(request, user)
                return render(request, "home.html", {"mensaje" : f"Bienvenido {user.get_username()}"})
            else:
                return fallo
        else:
            return fallo

    else:
        return render(request, "login.html", {"formulario" : AuthenticationForm()})



# def register(request):
#     if request.method == "POST":
#         formulario = UserRegisterForm(request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             return render(request, "home.html", {"mensaje" : f"Usuario {formulario.cleaned_data["username"]} creado correctamente"})
#         else:
#             return render(request, "register.html", {"mensaje" : "Usuario o contraseña incorrectos", "formulario" : UserRegisterForm()})

#     else:
#         return render(request, "register.html", {"formulario" : UserRegisterForm()})



class Logout(LoginRequiredMixin, LogoutView):
    template_name = "home.html"
    extra_context = {"mensaje" : "Te deslogueaste correctamente"}



# @login_required
# def editar_perfil(request):
#     usuario = request.user
#     formulario_viejo = UserEditForm(instance = usuario)
#     if request.method == "POST":
#         formulario_nuevo = UserEditForm(request.POST)
#         if formulario_nuevo.is_valid():
#             info = formulario_nuevo.cleaned_data
#             usuario.email = info["email"]
#             usuario.password1 = info["password1"]
#             usuario.password2 = info["password2"]
#             usuario.first_name = info["first_name"]
#             usuario.last_name = info["last_name"]
#             usuario.save()
#             return render(request, "get_perfil.html", {"usuario" : usuario, "mensaje" : "Usuario editado correctamente"})
#         else:
#             return render(request, "editar_perfil.html", {"formulario" : formulario_viejo, "mensaje" : "Datos inválidos, vuelda a intentarlo"})

#     else:
#         return render(request, "editar_perfil.html", {"formulario" : formulario_viejo})



@login_required
def eliminar_perfil(request):
    usuario = request.user
    usuario.delete()
    return render(request, "home.html", {"mensaje" : "Usuario eliminado correctamente"})

##########################################