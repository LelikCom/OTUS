# 1. Используем официальный образ Python
FROM python:3.10-bookworm

# 2. Указываем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Копируем файл зависимостей
COPY requirements.txt .

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь код приложения внутрь контейнера
COPY . .

# 6. Открываем порт 8000
EXPOSE 8000

# 7. Запускаем сервер
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
