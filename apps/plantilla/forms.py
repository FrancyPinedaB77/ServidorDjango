from django import forms

class forms_inicio(forms.Form):
    usuario = forms.CharField(label='usuario', max_length=20)
    numtuits = forms.CharField(label='numtuits', max_length=20)
    otro = forms.CharField(label='otro', max_length=20)


 