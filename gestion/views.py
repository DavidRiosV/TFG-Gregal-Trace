from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404, render

from .models import Proyecto

# Apartados de listado: traduce la palabra de la URL al código guardado en la base de datos.
TIPOS = {
    'obras': {'codigo': 'OBR', 'titulo': 'Obras', 'imagen': 'img/categorias/obras.jpg'},
    'intervenciones': {'codigo': 'INT', 'titulo': 'Intervenciones', 'imagen': 'img/categorias/intervenciones.jpg'},
    'mantenimientos': {'codigo': 'MAN', 'titulo': 'Mantenimientos', 'imagen': 'img/categorias/mantenimientos.jpg'},
}


def datos_menu():
    """Datos del menú y del inicio: cada tipo de trabajo con sus proyectos en proceso y terminados."""
    nav_tipos = {}
    for slug, datos in TIPOS.items():
        nav_tipos[slug] = {
            'titulo': datos['titulo'],
            'imagen': datos['imagen'],
            'en_proceso': Proyecto.objects.filter(tipo=datos['codigo'], estado='PRO').count(),
            'terminados': Proyecto.objects.filter(tipo=datos['codigo'], estado='TER').count(),
        }
    return nav_tipos


def pagina_del_tipo(proyecto):
    """Listado al que pertenece un proyecto: (slug, título)."""
    for slug, datos in TIPOS.items():
        if datos['codigo'] == proyecto.tipo:
            return slug, datos['titulo']
    return None, 'Inicio'


def index(request):
    return render(request, 'gestion/index.html', {
        'nav_tipos': datos_menu(),
        'seccion': 'inicio',
    })


def lista_proyectos(request, tipo):
    # La URL solo acepta obras, intervenciones o mantenimientos (re_path en urls.py)
    datos_tipo = TIPOS[tipo]
    proyectos = Proyecto.objects.filter(tipo=datos_tipo['codigo']).order_by('-fecha_inicio', '-id')

    # Filtro por estado: en proceso (por defecto), terminados o todos
    estado = request.GET.get('estado', 'PRO')
    if estado not in ('PRO', 'TER', 'todos'):
        estado = 'PRO'
    if estado != 'todos':
        proyectos = proyectos.filter(estado=estado)

    # Buscador por nombre o descripción (Q con | para hacer un OR)
    busqueda = request.GET.get('q', '').strip()
    if busqueda:
        proyectos = proyectos.filter(
            Q(nombre__contains=busqueda) | Q(descripcion__contains=busqueda)
        )

    return render(request, 'gestion/lista_proyectos.html', {
        'proyectos': proyectos,
        'titulo': datos_tipo['titulo'],
        'slug': tipo,
        'busqueda': busqueda,
        'estado_actual': estado,
        'nav_tipos': datos_menu(),
        'seccion': tipo,
    })


def detalle_proyecto(request, pk):
    """Detalle de un proyecto en modo consulta: datos, apuntes y total de horas."""
    proyecto = get_object_or_404(Proyecto.objects.select_related('creado_por'), pk=pk)

    consumos = proyecto.consumos.select_related('material', 'trabajador').order_by('-fecha', '-id')
    horas = consumos.filter(material__unidad='H').aggregate(Sum('cantidad'))['cantidad__sum']
    if horas is None:
        horas = 0

    slug, texto_volver = pagina_del_tipo(proyecto)

    return render(request, 'gestion/detalle_proyecto.html', {
        'proyecto': proyecto,
        'consumos': consumos,
        'horas': horas,
        'slug_volver': slug,
        'texto_volver': texto_volver,
        'nav_tipos': datos_menu(),
        'seccion': slug,
    })
