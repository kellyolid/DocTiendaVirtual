from web_final.models import UserProfile, Producto, Categoria
from django.contrib.auth.models import User
from django import forms
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('category','nombre','descripcion','precio','imagen')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre','descripcion')
