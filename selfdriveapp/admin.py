

# Register your models here.
from django.contrib import admin
from selfdriveapp.models import Product
# Register your models here.
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','location','category','pickdate','is_active']
    ordering=['id']
    list_filter=['category','is_active']
    
admin.site.register(Product,ProductAdmin)