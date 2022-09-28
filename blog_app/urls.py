from django.urls import path
from .views import *


urlpatterns = [
    ########### URLS PRINCIPALES ###########
    # path('', home, name="home"),
    # path('about/', about, name="about"),
    # path('pages/', pages, name="pages"),
    ########################################

    ########### URLS PUBLICACIONES ##########
    # path('pages/<id>', get_page, name="get_page"),
    # path('pages/crear/', crear_page, name="crear_page"),
    # path('pages/editar/<id>', editar_page, name="editar_page"),
    # path('pages/eliminar/<id>', eliminar_page, name="eliminar_page"),
    ########################################

    ############# URLS USUARIO #############
    # path('perfil/', get_perfil, name="get_perfil"),
    # path('perfil/login/', login, name="login"),
    # path('perfil/register/', register, name="register"),
    # path('perfil/logout/', Logout.as_view(), name="logout"),
    # path('perfil/editar/', editar_perfil, name="editar_perfil"),
    # path('perfil/eliminar/', eliminar_perfil, name="eliminar_perfil"),
    ########################################
]