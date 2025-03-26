"""
Модуль для асинхронной инициализации базы данных и заполнения данными.

Выполняет следующие шаги:
  1. Создает таблицы (если они отсутствуют) на основе моделей.
  2. Загружает данные пользователей и постов через API (jsonplaceholder_requests).
  3. Вставляет пользователей и посты в базу данных с проверкой наличия постов.
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from models import Base, engine, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect, text

# Создаем асинхронную фабрику сессий
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables() -> None:
    """
    Проверяет наличие таблиц 'users' и 'posts' в базе данных.
    Если хотя бы одна из таблиц отсутствует, создает их.
    """
    async with engine.begin() as conn:
        def check_and_create(sync_conn):
            inspector = inspect(sync_conn)
            # Проверяем наличие обеих таблиц
            if not inspector.has_table("users") or not inspector.has_table("posts"):
                print("Таблицы не найдены. Создаём users и posts...")
                Base.metadata.create_all(bind=sync_conn)
            else:
                print("Таблицы уже существуют. Пропускаем создание.")

        await conn.run_sync(check_and_create)


async def insert_users(session: AsyncSession, users_data: list[dict]) -> None:
    """
    Вставляет список пользователей в базу данных.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        users_data (list[dict]): Список словарей с данными пользователей.
    """
    users = [
        User(
            name=user["name"],
            username=user["username"],
            email=user["email"],
        )
        for user in users_data
    ]
    session.add_all(users)
    await session.commit()


async def insert_posts(session: AsyncSession, posts_data: list[dict]) -> None:
    """
    Вставляет список постов в базу данных.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        posts_data (list[dict]): Список словарей с данными постов.
    """
    posts = [
        Post(
            user_id=post["userId"],
            title=post["title"],
            body=post["body"],
        )
        for post in posts_data
    ]
    session.add_all(posts)
    await session.commit()


async def check_and_insert_posts(session: AsyncSession, posts_data: list[dict]) -> None:
    """
    Проверяет, существуют ли посты с ID от 1 до 100.
    Если такие посты отсутствуют, вставляет данные из posts_data.

    Args:
        session (AsyncSession): Асинхронная сессия SQLAlchemy.
        posts_data (list[dict]): Список словарей с данными постов.
    """
    result = await session.execute(
        text("SELECT id FROM posts WHERE id BETWEEN 1 AND 100")
    )
    existing_posts = result.fetchall()

    if existing_posts:
        print("Посты с id 1–100 уже есть. Пропускаем вставку.")
    else:
        print("Постов нет. Вставляем в базу.")
        await insert_posts(session, posts_data)


async def async_main() -> None:
    """
    Выполняет асинхронный цикл инициализации базы данных:
      - Создает таблицы, если они отсутствуют.
      - Загружает данные пользователей и постов.
      - Вставляет пользователей и посты в базу данных.
    """
    print("Запуск инициализации базы данных...")
    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(), fetch_posts_data()
    )

    async with AsyncSessionLocal() as session:
        print("👥 Добавляем пользователей...")
        await insert_users(session, users_data)

        print("Проверяем и добавляем посты...")
        await check_and_insert_posts(session, posts_data)

    print("Инициализация завершена.")


def main() -> None:
    """
    Точка входа для асинхронной инициализации базы данных.
    """
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
