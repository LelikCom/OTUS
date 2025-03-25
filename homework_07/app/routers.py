from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Post, User

# Главная страница для отображения всех постов
@app.route('/')
def index():
    # Извлекаем все посты и связываем с пользователями через user_id
    posts = db.session.query(Post, User).join(User, Post.user_id == User.id).all()

    # Передаем посты в шаблон
    return render_template('index.html', posts=posts)

# Маршрут для добавления поста
@app.route('/add', methods=['POST'])
def add_post():
    # Получаем данные из формы
    title = request.form.get('title')
    body = request.form.get('body')
    author_name = request.form.get('author_name')  # имя и фамилия автора из формы

    # Проверяем, существует ли автор в базе данных
    user = db.session.query(User).filter(User.name == author_name).first()

    if user:
        # Если автор найден, создаем пост с данным автором
        new_post = Post(title=title, body=body, user_id=user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('Пост успешно добавлен!', 'success')
        return redirect(url_for('index'))  # Перенаправляем на главную страницу
    else:
        # Если автора нет, предлагаем создать нового пользователя
        flash(f'Автор с именем "{author_name}" не найден. <a href="{{ url_for("create_author") }}">Создать нового автора?</a>', 'danger')
        return redirect(url_for('index'))  # Перенаправляем обратно на главную страницу, с flash-сообщением

# Маршрут для создания нового автора
@app.route('/create_author', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        # Получаем данные для создания нового пользователя
        author_name = request.form.get('author_name')
        email = request.form.get('email')

        # Проверяем, существует ли уже такой пользователь
        existing_user = db.session.query(User).filter(User.name == author_name).first()
        if existing_user:
            flash(f'Автор с именем "{author_name}" уже существует!', 'danger')
            return redirect(url_for('create_author'))  # Если автор существует, возвращаем на создание нового

        # Если пользователя нет, создаем нового
        new_user = User(name=author_name, email=email)
        db.session.add(new_user)
        db.session.commit()

        flash(f'Новый пользователь {author_name} успешно создан!', 'success')
        return redirect(url_for('add_post'))  # Перенаправление на страницу добавления поста
    return render_template('create_author.html')  # Шаблон для создания автора
