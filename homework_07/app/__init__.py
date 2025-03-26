"""
Инициализация Flask-приложения, подключение к базе данных и настройка миграций.

Загружает переменные окружения из файла .env, конфигурацию из класса Config,
инициализирует SQLAlchemy и Flask-Migrate, а также импортирует маршруты.
"""

import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Загружаем переменные окружения из файла .env
load_dotenv()

# Создание экземпляра Flask-приложения
app = Flask(__name__)

# Загрузка конфигурации из класса Config в модуле app.config
app.config.from_object("app.config.Config")

# Инициализация SQLAlchemy и Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Логирование ключевых переменных окружения для отладки
print("=== Проверка конфигурации ===")
print("DATABASE_URL:", os.getenv("DATABASE_URL"))
print("SQLALCHEMY_DATABASE_URI:", app.config.get("SQLALCHEMY_DATABASE_URI"))

# Импорт маршрутов для регистрации эндпоинтов
from app import routers  # noqa: E402, F401
