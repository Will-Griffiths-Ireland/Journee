from django.contrib import admin
from .models import Journal


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'journal_date',
        'content',
        'is_public',
        'self_image',
        'day_image',
    )
    list_filter = ('user', 'journal_date')
