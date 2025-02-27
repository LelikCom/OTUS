# FastAPI + Docker

Этот проект представляет собой простое веб-приложение на **FastAPI**, которое контейнеризовано с использованием **Docker**.

---
## 📌 Функциональность
Приложение содержит один маршрут:
- `GET /ping/` – возвращает JSON-ответ `{ "message": "pong" }`

---
## 🛠 Установка и запуск

### 🔹 1. Клонирование репозитория
```bash
git clone https://github.com/LelikCom/OTUS
cd OTUS
cd homework_06
```

---
## 🚀 Запуск в Docker

### **1. Собрать Docker-образ**
```bash
docker build -t fastapi-app .
```

### **2. Запустить контейнер**
#### **Windows (PowerShell / CMD)**
```bash
docker run -d -p 8000:8000 fastapi-app
```

#### **Linux/macOS (Bash/Zsh)**
```bash
docker run -d -p 8000:8000 fastapi-app
```

После этого API будет доступно по адресу:
👉 **http://localhost:8000/ping/**

### **3. Проверка работы контейнера**
#### **Через браузер**
Перейдите по адресу: **http://localhost:8000/ping/**

#### **Через терминал (cURL)**
```bash
curl http://localhost:8000/ping/
```

---
## 📌 Управление контейнером

### **Посмотреть запущенные контейнеры**
```bash
docker ps
```

### **Остановить контейнер**
```bash
docker stop <CONTAINER_ID>
```
Или сразу все контейнеры:
```bash
docker stop $(docker ps -q)
```

### **Удалить контейнер**
```bash
docker rm <CONTAINER_ID>
```

### **Удалить образ**
```bash
docker rmi fastapi-app
```

---
## 🚀 Дополнительно
- 📌 **Авторизация в Docker Hub (если нужно):**
```bash
docker login
```
- 📌 **Очистка неиспользуемых образов и контейнеров:**
```bash
docker system prune -a
```