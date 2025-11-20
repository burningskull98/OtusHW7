"""
Этот модуль отвечает за настройку административного интерфейса приложения.
"""
from django.contrib import admin
from .models import Post, Comment, User, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "pub_date", )
    ordering = ("pub_date",)
    list_filter = ("user",)
    search_fields = ("title", "content")
    search_help_text = "Поиск по названию и содержимому"

    fields = ("title", "content", "user", )


class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "profile"]
    search_fields = ["name"]
    search_help_text = "Введите имя пользователя или его профиль"

    @staticmethod
    def profile(obj):
        return obj.profile if obj.profile else "Нет профиля"


admin.site.register(User, UserAdmin)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    search_help_text = "Введите название тега"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "user", "post", "pub_date"]
    list_filter = ["post", "user"]
    search_fields = ["text", "user"]
    search_help_text = (
        "Поиск по тексту комментария, имени пользователя и названию поста"
    )
