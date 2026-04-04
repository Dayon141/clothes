from django.contrib import admin
from .models import Clothes, Brand, Size, Color

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Size)

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['Brand', 'title']
    list_display_links = ['Brand']
    search_fields = ['title']
    list_filter = ['Brand', 'size', 'color']
    list_editable = ['title']

admin.site.register(Clothes, admin_class=ClothesAdmin)