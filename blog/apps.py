"""
Этот модуль отвечает за конфигурацию приложений в проекте.
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Конфигурация приложения для блога
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
