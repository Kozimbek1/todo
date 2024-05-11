from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['todo_name', 'body']
    list_filter = ['created', 'updated']
    list_display = ['todo_name', 'status']
    list_display_links = ['todo_name']
    list_editable = ['status']
    list_per_page = 100
    ordering = ['created', 'updated', 'todo_name']
    save_on_top = True