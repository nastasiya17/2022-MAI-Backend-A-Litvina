from django.contrib import admin
from showplace.models import Showplace

class ShowplaceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category_id")
    
admin.site.register(Showplace, ShowplaceAdmin)

