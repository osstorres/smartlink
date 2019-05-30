from django import forms
from .models import *
from .choices import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import (
    UNUSABLE_PASSWORD_PREFIX, identify_hasher,
)
from django.utils.translation import gettext, gettext_lazy as _
class ReadOnlyPasswordHashWidget(forms.Widget):
    template_name = 'auth/widgets/read_only_password_hash.html'
    read_only = False

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        summary = []
        if not value or value.startswith(UNUSABLE_PASSWORD_PREFIX):
            summary.append({'label': gettext("No password set.")})
        else:
            try:
                hasher = identify_hasher(value)
            except ValueError:
                summary.append()
            else:
                for key, value_ in hasher.safe_summary(value).items():
                    summary.append('')
        context['summary'] = summary
        return context


class ReadOnlyPasswordHashField(forms.Field):
    widget = ReadOnlyPasswordHashWidget

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("required", False)
        super().__init__(*args, **kwargs)

    def bound_data(self, data, initial):
        # Always return initial because the widget doesn't
        # render an input field.
        return initial

    def has_changed(self, initial, data):
        return False
class UserChangeForm(forms.ModelForm):
 
    password = ReadOnlyPasswordHashField(label="",
        #help_text="Puedes cambiar la contraseña con este formulario : <a href=\"password/\"> cambiar contraseña </a>.")
        help_text="")
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Contraseña",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma la contraseña",
        widget=forms.PasswordInput,
        help_text="")

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class SendEmailForm(forms.Form):
    asunto = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ('Asunto')}))
    mensaje =  forms.CharField(widget=CKEditorWidget())
    users = forms.ModelMultipleChoiceField(label="Destinatarios",
                                           queryset=Clientes.objects.all(),
                                           widget=forms.SelectMultiple())


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
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
            'password2',
 
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
            #'email',
            
            #'last_name',
            #'password',
        )
        


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
    


    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}) )
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    #correo = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    telefono_celular = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    #telefono = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    sexo = forms.ChoiceField(choices= SEXO_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    ocupacion = forms.ChoiceField(choices= OCUPACION_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    empresa = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    puesto = forms.ChoiceField(choices = PUESTO_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    estado = forms.ChoiceField(choices = ESTADO_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    relacion_tec = forms.ChoiceField(choices = RELACION_TEC_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
   


    class Meta:
        model = Clientes
        fields =[

    'nombre', 
    'apellidos',
    'correo', 
    'telefono_celular',
    #'telefono',
    'sexo',
    'ocupacion',
    'empresa', 
    'puesto',
    'estado',
    'ciudad',
    'relacion_tec',
   

        ]

