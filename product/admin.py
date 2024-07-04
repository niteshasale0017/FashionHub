from django.contrib import admin
from .models import Shirt,Pant,Shoe
# Register your models here.
@admin.register(Shirt)
class ShirtAdmin(admin.ModelAdmin):
    list_display=('name','shirt_type','size_m','size_l','size_xl','price','discount','image','status','description')

@admin.register(Pant)
class PantAdmin(admin.ModelAdmin):
    list_display=('name','pant_type','size_28','size_30','size_32','size_34','price','discount','image','status','description')

@admin.register(Shoe)
class ShoeAdmin(admin.ModelAdmin):
    list_display=('name','shoe_type','size_7','size_8','size_9','size_10','price','discount','image','status','description')

