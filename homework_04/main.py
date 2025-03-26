"""
Основной модуль: создает таблицы, загружает данные и сохраняет их в базу.
"""

from sqlalchemy import text
import asyncio
from models import Base, engine, Session, User, Post
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def create_tables() -> None:
    """
    Создание таблиц в БД (drop + create).
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def insert_users(session: Session, users_data: list[dict]) -> None:
    """
    Добавить список пользователей в БД.

    :param session: сессия SQLAlchemy
    :param users_data: список словарей с данными пользователей
    """
    users = [
        User(
            id=user["id"],
            name=user["name"],
            username=user["username"],
            email=user["email"],
        )
        for user in users_data
    ]
    session.add_all(users)
    await session.commit()


async def insert_posts(session: Session, posts_data: list[dict]) -> None:
    """
    Добавить список постов в БД.

    :param session: сессия SQLAlchemy
    :param posts_data: список словарей с данными постов
    """
    posts = [
        Post(
            id=post["id"],
            user_id=post["userId"],
            title=post["title"],
            body=post["body"],
        )
        for post in posts_data
    ]
    session.add_all(posts)
    await session.commit()


async def async_main() -> None:
    """
    Выполнить полный асинхронный цикл:
    - создать таблицы
    - загрузить пользователей и посты
    - сохранить данные в БД
    - обновить sequence
    """
    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(), fetch_posts_data()
    )

    async with Session() as session:
        await insert_users(session, users_data)
        await insert_posts(session, posts_data)

        # Обновляем sequence, чтобы избежать конфликта ID
        await session.execute(text("SELECT setval('posts_id_seq', (SELECT MAX(id) FROM posts))"))
        await session.commit()


def main() -> None:
    """
    Точка входа: запускает async_main с помощью asyncio.run().
    """
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
