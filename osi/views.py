from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import formulario

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        aa = form_data.get("usuario")
        bb = form_data.get("solicitante")
        cc = form_data.get("centro_de_costo")
        dd = form_data.get("anexo")
        ee = form_data.get("asunto")

        objh = formulario.objects.create(usuario = aa, solicitante= bb, centro_de_costo =cc, anexo=dd,asunto=ee)
    context={
        "el_form":form,
    }
    return render(request, "base.html",context)
