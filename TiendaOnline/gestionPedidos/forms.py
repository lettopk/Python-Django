from django import forms

#Se establecen los campos para el formulario

class formulario_contacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()