from django import forms

class usuario(forms.Form):
    usuario = forms.CharField(label='usuario', max_length=20)

class numtuits(forms.Form):
    numtuits = forms.CharField(label='numtuits', max_length=20)


class otro(forms.Form):
    otro = forms.CharField(label='otro', max_length=20)