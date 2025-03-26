"""
Маршруты Flask-приложения.

Этот модуль определяет следующие маршруты:
    - Главная страница (index): отображение всех постов с данными об авторах.
    - Добавление поста (add_post): создание нового поста, если автор найден.
    - Форма создания нового автора (create_author, GET): отображение формы для ввода данных нового автора.
    - Обработка создания нового автора (create_author_post, POST): сохранение нового автора в базе данных.
"""

from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Post, User


@app.route("/")
def index():
    """
    Главная страница.

    Извлекает все посты и соответствующих пользователей из базы данных,
    а затем рендерит шаблон 'index.html'.

    Returns:
        Отрендеренный HTML-шаблон главной страницы.
    """
    posts = db.session.query(Post, User).join(User, Post.user_id == User.id).all()
    return render_template("index.html", posts=posts)


@app.route("/add", methods=["POST"])
def add_post():
    """
    Добавление нового поста.

    Принимает данные из формы (заголовок, тело, имя автора) и пытается найти автора в базе.
    Если автор найден, создает и сохраняет новый пост.
    Если автора нет, перенаправляет на форму создания нового автора.

    Returns:
        Перенаправление на главную страницу или на форму создания автора.
    """
    title = request.form.get("title")
    body = request.form.get("body")
    author_name = request.form.get("author_name")

    user = db.session.query(User).filter(User.name == author_name).first()

    if user:
        new_post = Post(title=title, body=body, user_id=user.id)
        db.session.add(new_post)
        db.session.commit()
        flash("Пост успешно добавлен!", "success")
        return redirect(url_for("index"))
    else:
        flash(f'Автор "{author_name}" не найден. Пожалуйста, добавьте его.', "warning")
        return redirect(url_for("create_author", name=author_name))


@app.route("/create_author")
def create_author():
    """
    Форма создания нового автора.

    Извлекает имя из параметров URL (если передано) и рендерит шаблон 'create_author.html'
    для ввода данных нового автора.

    Returns:
        Отрендеренный HTML-шаблон формы создания автора.
    """
    name = request.args.get("name", "")
    return render_template("create_author.html", name=name)


@app.route("/create_author", methods=["POST"])
def create_author_post():
    """
    Обработка формы создания нового автора.

    Принимает данные из формы (имя, username, email), создает нового пользователя и сохраняет его.
    После успешного сохранения перенаправляет на главную страницу.

    Returns:
        Перенаправление на главную страницу.
    """
    name = request.form.get("name")
    username = request.form.get("username")
    email = request.form.get("email")

    new_user = User(name=name, username=username, email=email)
    db.session.add(new_user)
    db.session.commit()

    flash(f'Автор "{name}" успешно добавлен!', "success")
    return redirect(url_for("index"))
