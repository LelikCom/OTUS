"""
Конфигурационный файл Flask-приложения.

Загружает настройки из переменных окружения с использованием dotenv.
"""

import os
from dotenv import load_dotenv

# Автоматически загружает переменные из .env в окружение
load_dotenv()


class Config:
    """
    Основной класс конфигурации приложения.

    Значения берутся из переменных окружения или задаются по умолчанию.
    """

    # Строка подключения к базе данных PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/appdb"
    )

    # Отключение отслеживания изменений объектов SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Режим запуска Flask-приложения (development, production)
    FLASK_ENV = os.getenv("FLASK_ENV", "production")

    # Секретный ключ приложения (используется для сессий и защиты форм)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_default_secret")
