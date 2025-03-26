"""
Модуль моделей для асинхронной работы с PostgreSQL через SQLAlchemy.
"""

import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# Загружаем переменные окружения
load_dotenv()

PG_CONN_URI = os.getenv("SQLALCHEMY_PG_CONN_URI")
print("Подключение к БД:", PG_CONN_URI)

engine = create_async_engine(PG_CONN_URI, echo=True)
Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class User(Base):
    """
    SQLAlchemy модель пользователя (таблица users).

    Поля:
        id (int): первичный ключ
        name (str): имя пользователя
        username (str): логин
        email (str): электронная почта
        posts: связь с моделью Post (один ко многим)
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    """
    SQLAlchemy модель поста (таблица posts).

    Поля:
        id (int): первичный ключ
        user_id (int): внешний ключ к users.id
        title (str): заголовок поста
        body (str): содержимое поста
        user: связь с моделью User
    """

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

    user = relationship("User", back_populates="posts")
