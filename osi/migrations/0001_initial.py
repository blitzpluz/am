# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-18 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default=None, max_length=30, null=True)),
                ('solicitante', models.CharField(blank=True, default=False, max_length=30)),
                ('centro_de_costo', models.CharField(max_length=30)),
                ('anexo', models.CharField(default=False, max_length=10)),
                ('asunto', models.TextField()),
                ('status_ticket', models.CharField(choices=[('a', 'abierto'), ('b', 'cerrado'), ('c', 'asignado'), ('d', 'pendiente'), ('e', 'en proceso')], default='c', max_length=1)),
                ('fecha_inicio_ticket', models.DateTimeField(auto_now_add=True)),
                ('fecha_solucion_ticket', models.DateTimeField(blank=True, null=True)),
                ('tiempo_solucion', models.CharField(blank=True, max_length=10)),
                ('fuente_ticket', models.CharField(choices=[('P', 'C.A.U-Paipote'), ('I', 'Informatica fomento'), ('S', 'C.A.U-Sistemas'), ('C', 'C.A.U'), ('N', 'NN')], default='P', max_length=1)),
                ('servicio_ti_tecnico', models.CharField(choices=[('a', 'NN'), ('b', 'administracion de base de datos'), ('c', 'almacenamiento storage/fileserver'), ('d', 'aplicaciones web'), ('e', 'autenticacion cuentas acceso'), ('f', 'correo electronico'), ('g', 'data center espacio-poder-clima '), ('h', 'desarollo Sias'), ('i', 'internet isp'), ('j', 'mantencion sias'), ('k', 'mesa de servicio'), ('l', 'monitoreo '), ('m', 'multifuncional impresion-impresora-escaner'), ('n', 'ofimatica estacion trabajo-software'), ('o', 'procesamiento de datos servidores'), ('p', 'proyeccion c/s sala'), ('q', 'punto de red'), ('r', 'redes MPLS wan'), ('s', 'redes lan'), ('t', 'respaldo y recuperacion'), ('u', 'seguridad periometral e interna'), ('v', 'soporte sias'), ('w', 'telefonia ip publica movil y analoga '), ('x', 'video conferencia/camaras'), ('y', 'explotacion de sitemas'), ('z', 'control automatico')], default='a', max_length=1)),
                ('servicio_ti_de_cara_al_usuario', models.CharField(choices=[('a', 'NN'), ('b', 'informacion para toma de decisiones'), ('c', 'navegacion web internet-intranet '), ('d', 'colaboracion y comunicacion'), ('e', 'impresion fotocopiado escaner o fax'), ('f', 'ofimatica basica puesto de trabajo')], default='a', max_length=1)),
                ('reparticion', models.CharField(choices=[('a', 'paipote'), ('b', 'NN'), ('c', 'antofagasta'), ('d', 'rancagua'), ('e', 'santiago'), ('f', 'coquimbo'), ('g', 'amalia'), ('h', 'arica'), ('i', 'barriles'), ('j', 'cabildo'), ('k', 'calama'), ('l', 'camarones'), ('m', 'catemu'), ('n', 'copiapo'), ('o', 'delta'), ('p', 'el arenal'), ('q', 'el salado'), ('r', 'illapel'), ('s', 'la serena'), ('t', 'las cenizas'), ('u', 'las luces'), ('v', 'mantos blancos'), ('w', 'matta'), ('x', 'ovalle'), ('y', 'panulcillo'), ('z', 'rumano chileno'), ('ab', 'taltal'), ('ac', 'tocopilla'), ('ad', 'vallenar'), ('ae', 'ventanas')], default='a', max_length=1)),
                ('medio_solicitud', models.CharField(choices=[('a', 'correo'), ('b', 'telefono'), ('d', 'web')], default='a', max_length=1)),
                ('sia', models.CharField(blank=True, max_length=30)),
                ('observacion', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_tecnico', models.CharField(default=False, max_length=30)),
                ('anexo', models.CharField(default=None, max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='formulario',
            name='atendido_por',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='osi.tecnico'),
        ),
    ]
