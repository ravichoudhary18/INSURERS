from django.contrib import admin
from file.models import File

class FileAdmin(admin.ModelAdmin):
    # Display fields in the list view
    list_display = ('file_id', 'file', 'created_at', 'created_by', 'updated_at', 'updated_by')
    
    # Add search functionality
    search_fields = ('file', 'created_by__username', 'updated_by__username')
    
    # Add filter options
    list_filter = ('created_at', 'updated_at', 'created_by', 'updated_by')
    
    # Set fields to be read-only
    readonly_fields = ('created_at', 'updated_at')

    # Specify fields to display in the detail view
    fields = ('file', 'created_by', 'updated_by', 'created_at', 'updated_at')

admin.site.register(File, FileAdmin)