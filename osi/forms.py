from django import forms


class ContactForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'siga el ejemplo: P.Rivera'}))
    solicitante = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'rellenar en caso de que no sea para usted la atencion'}))

    centro_de_costo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'ejemplo : 01-1020'}))
    anexo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'su anexo telefonico'}))
    asunto = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'explique lo que necesita  y sea conciso'}))
