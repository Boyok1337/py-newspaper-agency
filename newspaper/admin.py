from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Redactor, Topic, Newspaper


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "years_of_experience",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "email",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "years_of_experience",
                ),
            }
        ),
    )
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    list_filter = ("published_date", "topics")
    search_fields = ("title", "content")
    filter_horizontal = ("topics", "publishers")
