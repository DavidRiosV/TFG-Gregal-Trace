from django.contrib import admin

from .models import Albaran, Consumo, Material, Oficina, Operario, Proyecto, Usuario

admin.site.register(Usuario)
admin.site.register(Operario)
admin.site.register(Oficina)
admin.site.register(Proyecto)
admin.site.register(Material)
admin.site.register(Consumo)
admin.site.register(Albaran)
