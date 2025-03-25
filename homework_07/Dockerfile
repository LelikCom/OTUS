# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Настройка порта для Flask
EXPOSE 8000

# Команда для запуска приложения через gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
