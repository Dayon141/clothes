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

    def image_admin(self,obj):
        if obj.image1:
            return format_html('<img src="{}" width="50" height="50" />', obj.image1.url)
        return "Suwret joq"
    image_admin.short_description = 'Image'

admin.site.register(Clothes, admin_class=ClothesAdmin)