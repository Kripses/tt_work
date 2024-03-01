from django.contrib import admin

from file_manager.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file', 'uploaded_at', 'processed', ]
