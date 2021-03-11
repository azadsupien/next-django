from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    display = ('name', ' Email ', ' password', 'id')

admin.site.register(Todo , TodoAdmin)