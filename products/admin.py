from django.contrib import admin
from . import models


# Register your models here.

class ProductImageInLine(admin.TabularInline):
    model = models.ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_top', 'is_active')
    list_filter = ('title', 'is_top', 'is_active')
    list_editable = ('is_top', 'is_active')
    search_fields = ('title','is_top', 'is_active')
    inlines = (ProductImageInLine,)


admin.site.register(models.ProductImage)
admin.site.register(models.Product, ProductAdmin)
