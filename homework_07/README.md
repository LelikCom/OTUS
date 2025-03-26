# 📝 Flask Blog App (Homework 07)

Веб-приложение на Flask, развёрнутое в Docker. Позволяет просматривать посты, создавать новые и добавлять авторов, если их ещё нет.

---

## 🚀 Как запустить

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo/homework_07
```

> 🔁 Замените ссылку на актуальную, если используете другой репозиторий.

---

### 2. Создайте `.env` файл в корне проекта (`homework_07/.env`)

```env
# Пример .env файла
DATABASE_URL=postgresql://your_user:your_password@db:5432/appdb
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
SQLALCHEMY_PG_CONN_URI=postgresql+asyncpg://your_user:your_password@db:5432/appdb
```



---

### 3. Запустите контейнеры Docker

```bash
docker-compose up --build
```

Если `docker-compose.yml` находится в `homework_07`, убедитесь, что запускаете команду из этой папки.

---

### 4. Откройте в браузере

```
http://localhost:5000
```

---

## ✨ Возможности приложения

- 📄 Просмотр всех постов
- ➕ Создание нового поста
- 👤 Автоматическое добавление нового автора, если его ещё нет

---

## 📦 Зависимости

Если хотите запустить вручную без Docker:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Требования

- Установленный Docker и Docker Compose
- Включён WSL2 (для Windows)
- Python 3.10+ (если запускается без Docker)

---