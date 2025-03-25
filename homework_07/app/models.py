from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'  # название таблицы
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    # связь с таблицей постов
    posts = relationship("Post", backref="user")


class Post(Base):
    __tablename__ = 'posts'  # название таблицы
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


# Настройка базы данных
engine = create_engine("postgresql://Lelik:89068874019@db:5432/appdb", echo=True)
Session = sessionmaker(bind=engine)
