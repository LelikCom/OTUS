# FastAPI Web App 🚀

Этот проект — небольшое веб-приложение на **FastAPI** с HTML-страницами и API.

## 📌 Функциональность
- 🌍 **Главная страница** `/`
- ℹ️ **Страница "О нас"** `/about/`
- 🔄 **REST API** `/api/items`

---

## 🚀 Установка и запуск  

### **🔹 Для Windows:**  
```powershell
git clone https://github.com/LelikCom/OTUS
cd OTUS/homework_05
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8080
```

---

### **🔹 Для Linux/macOS:**  
```bash
git clone https://github.com/LelikCom/OTUS
cd OTUS/homework_05
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8080
```

