from django.contrib import admin
from .models import Clothes, Brand, Size, Color

admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Size)

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['brand', 'title']
    list_display_links = ['brand']
    search_fields = ["brand"]
    list_filter = ["brand", "size", "color"]
    list_editable = ["title"]

admin.site.register(Clothes,admin_class = ClothesAdmin)