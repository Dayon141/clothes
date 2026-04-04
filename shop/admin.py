from django.contrib import admin
from .models import Clothes, Brand, Size, Color

admin.site.register(Clothes)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Size)
