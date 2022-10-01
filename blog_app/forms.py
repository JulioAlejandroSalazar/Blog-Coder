from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class PublicacionForm(forms.Form):
    titulo = forms.CharField(max_length=20)
    subtitulo = forms.CharField(max_length=20)
    contenido = RichTextUploadingField()

   
class BuscarPublicacionForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    contenido = forms.CharField(max_length=2000)
       

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 =  forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserRegisterForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento")

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "first_name", "last_name", "fecha_nacimiento"]


class UserFindForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField()
   
    
class UserChangeForm(UserChangeForm):
    Imagen= forms.ImageField (required=False)