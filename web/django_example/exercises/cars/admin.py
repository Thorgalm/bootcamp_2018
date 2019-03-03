from django.contrib import admin

# Register your models here.

from cars.models import Car, Engine


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "production_year"]
    search_fields = ["brand"]
    list_filter = ["brand", "model", "production_year", "body_type"]

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    pass



# admin.site.register(Car)
