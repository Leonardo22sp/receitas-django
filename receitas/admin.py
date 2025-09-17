# receitas/admin.py

from django.contrib import admin
from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categoria', 'created_at') # <-- ALTERADO
    list_display_links = ('id', 'title')
    list_filter = ('categoria',) # <-- ALTERADO
    search_fields = ('title', 'description')
    list_per_page = 25

admin.site.register(Receita, ReceitaAdmin)