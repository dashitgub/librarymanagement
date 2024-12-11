from django.contrib import admin
from .models import Library

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',) 
    list_editable = ('description')
    list_display_links = ('name')
    list_per_page = 20
    ordering = ('-created_at')
    actions = ['delete_selected_library']

    def delete_selected_library(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'{count} книга(-и) успешно удалены')

    delete_selected_library.short_description = 'Удалить выбранные книги'

    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at',)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_filter = ('created_at', 'category')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Дополнительная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ('created_at',)
