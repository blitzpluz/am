from django.contrib import admin

from .models import formulario,tecnico

admin.site.site_header ='MESA DE AYUDA INFORMATICA 2019" '
class personalizar(admin.ModelAdmin):
    list_display=["usuario","solicitante","centro_de_costo","anexo","atendido_por","asunto","status_ticket","fecha_inicio_ticket"]
    list_filter=["fecha_inicio_ticket","atendido_por","status_ticket"]
    search_fields=["usuario","solicitante","centro_de_costo","fecha_solucion_ticket"]
    class Meta:
        model= formulario,tecnico


class per(admin.ModelAdmin):
    list_display=["nombre_del_tecnico","anexo"]

    class Meta:
        model= tecnico




admin.site.register(formulario, personalizar)
admin.site.register(tecnico,per)
