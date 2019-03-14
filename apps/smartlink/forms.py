from django import forms
from .models import *
from .choices import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
    


    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), )
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    telefono_celular = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    telefono = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sexo = forms.ChoiceField(choices= SEXO_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    ocupacion = forms.ChoiceField(choices= OCUPACION_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    puesto = forms.ChoiceField(choices = PUESTO_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    estado = forms.ChoiceField(choices = ESTADO_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    relacion_tec = forms.ChoiceField(choices = RELACION_TEC_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = Clientes
        fields =[

    'nombre', 
    'apellidos',
    'correo', 
    'telefono_celular',
    'telefono',
    'sexo',
    'ocupacion',
    'empresa', 
    'puesto',
    'estado',
    'ciudad',
    'relacion_tec',
    'password',

        ]