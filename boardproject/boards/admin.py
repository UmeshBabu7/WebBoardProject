from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display=["name","description"]
    list_display_links=["name","description"]        

admin.site.register(Board,BoardAdmin)

