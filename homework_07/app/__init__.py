from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Указываем путь к конфигурации
app.config.from_object('app.config')  # Убедитесь, что config.py находится в папке app

# Конфигурация для PostgreSQL (с твоим логином и паролем)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://Lelik:89068874019@db:5432/appdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных и миграций
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Печатаем URL базы данных для проверки
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")

# Импортируем маршруты (предполагается, что маршруты находятся в app/routers.py)
from app import routers

# Возвращаем приложение для использования в других частях проекта
