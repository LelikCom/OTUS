import os


class Config:
    """Основные конфигурации приложения"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://Lelik:89068874019@db:5432/appdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'production'
