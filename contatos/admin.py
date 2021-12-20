from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'telefone', 'categoria', 'mostrar')
    list_filter = ('categoria', 'data_descricao')
    list_display_links = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
