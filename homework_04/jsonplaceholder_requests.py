"""
Асинхронные запросы к публичному API JSONPlaceholder.
"""

import aiohttp
from typing import Any, Dict, List

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: aiohttp.ClientSession, url: str) -> Any:
    """
    Асинхронно получить JSON с указанного URL.

    :param session: aiohttp-сессия
    :param url: URL для запроса
    :return: данные из ответа
    """
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.json()


async def fetch_users_data() -> List[Dict[str, Any]]:
    """
    Получить список пользователей из JSONPlaceholder API.

    :return: список словарей с данными пользователей
    """
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, USERS_DATA_URL)


async def fetch_posts_data() -> List[Dict[str, Any]]:
    """
    Получить список постов из JSONPlaceholder API.

    :return: список словарей с данными постов
    """
    async with aiohttp.ClientSession() as session:
        return await fetch_json(session, POSTS_DATA_URL)
