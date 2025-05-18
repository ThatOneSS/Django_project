from django.contrib import admin
from .models import Region, Company, Car
# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('name','status')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('name','status')
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model','company','region','price','color','km')
    list_filter = ('model','company','region','price','color','km','year','t_box','engine','fuel_type','vin','body_type')
    search_fields = ('model','company','region',)