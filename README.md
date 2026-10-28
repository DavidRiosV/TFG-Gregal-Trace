# Gregal Trace · Hito 1

Aplicación web con Django para **Instalaciones Gregal**: registro del material y las horas que se gastan en cada obra, intervención y mantenimiento.

Proyecto Integrado de 2.º DAW (IES Polígono Sur) · David Ríos Valencia.

## Qué incluye este hito (esqueleto)

- Estructura del proyecto Django: proyecto `mysite` y aplicación `gestion`.
- Modelo de datos completo con su migración: `Usuario` (hereda de `AbstractUser`), `Operario`, `Oficina`, `Proyecto`, `Material`, `Consumo` y `Albaran`.
- Panel de administración con todos los modelos registrados.
- Plantilla base (menú, cabecera y pie) con CSS propio y diseño adaptado a móvil.
- Plantillas reutilizables: buscador, migas de pan, estado del proyecto y botón de volver.
- Consulta de proyectos:
  - Inicio con acceso a cada sección y contadores de proyectos.
  - Listados de Obras, Intervenciones y Mantenimientos con buscador y filtro por estado.
  - Detalle de cada proyecto con sus apuntes y el total de horas.

El registro, el inicio de sesión, los permisos, la sesión y los formularios (CRUD) llegan en el Hito 2.

## Puesta en marcha

Requisitos: Python 3.12 y Git.

```bash
git clone https://github.com/DavidRiosV/TFG-Gregal-Trace.git
cd TFG-Gregal-Trace
git checkout hito-1

python -m venv myvenv
myvenv\Scripts\activate          # Windows
# source myvenv/bin/activate     # Linux / macOS

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Después, abre <http://127.0.0.1:8000>. Los datos se dan de alta desde <http://127.0.0.1:8000/admin>.

## Estructura

```text
├── manage.py
├── requirements.txt
├── mysite/                 # Configuración (settings.py, urls.py)
└── gestion/                # Aplicación principal
    ├── models.py           # Modelo de datos
    ├── views.py            # Inicio, listados, detalle y datos del menú
    ├── urls.py
    ├── admin.py
    ├── migrations/
    ├── static/             # CSS e imágenes
    └── templates/gestion/  # Plantillas
```

## Licencia

Proyecto académico, publicado para su evaluación. © 2026 David Ríos Valencia.
