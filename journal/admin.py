from django.contrib import admin
from .models import Journal, Profile


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "title",
        "journal_date",
        "content",
        "is_public",
        "self_image",
        "day_image",
    )
    list_filter = ("user", "journal_date")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "first_name",
        "last_name",
        "birthday",
        "account_activated",
        "make_new_page_public",
        "description_word_one",
        "description_word_two",
        "description_word_three",
        "colour_theme",
    )
    list_filter = ("user", "account_activated")
