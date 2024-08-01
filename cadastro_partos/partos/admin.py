from django.contrib import admin
from .models import Parto

@admin.register(Parto)
class PartoAdmin(admin.ModelAdmin):
    list_display = ('brinco', 'data_prov', 'data', 'ecc', 'tipo', 'manejo')
    search_fields = ('brinco', 'ecc', 'tipo')
    list_filter = ('tipo', 'data')