"""
Модели SQLAlchemy для пользователей и постов.

Определяет ORM-классы User и Post, связанные отношением "один ко многим".
"""

import os
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker,
)
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Базовый класс моделей SQLAlchemy
Base = declarative_base()

# Получаем URL базы данных из окружения
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user:password@localhost:5432/appdb"
)

# Создание движка и фабрики сессий
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)


class User(Base):
    """
    Модель пользователя.

    Атрибуты:
        id (int): Первичный ключ.
        name (str): Полное имя пользователя.
        username (str): Уникальное имя пользователя.
        email (str): Email-адрес.
        posts (List[Post]): Посты, связанные с этим пользователем.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    posts = relationship("Post", backref="user")


class Post(Base):
    """
    Модель поста.

    Атрибуты:
        id (int): Первичный ключ.
        title (str): Заголовок поста.
        body (str): Основной текст поста.
        user_id (int): Внешний ключ на пользователя.
    """

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
