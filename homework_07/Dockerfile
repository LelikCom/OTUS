# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Устанавливаем рабочую директорию и выполняем миграции, затем запускаем приложение
CMD bash -c "flask db upgrade && python db_filling/main.py && gunicorn -b 0.0.0.0:8000 app:app"
