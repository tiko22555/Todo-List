from django.contrib import admin
from .models import Todo


class AdminTodo(admin.ModelAdmin):
    list_display = ("title", "deadline", "status")
    ordering = ["-deadline"]
    

admin.site.register(Todo, AdminTodo)
