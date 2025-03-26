import os
from logging.config import fileConfig
from sqlalchemy import create_engine
from alembic import context
from app.models import Base

config = context.config
alembic_ini_path = os.path.join(os.path.dirname(__file__), '../alembic.ini')
if os.path.exists(alembic_ini_path):
    fileConfig(alembic_ini_path)
else:
    import logging
    logging.basicConfig(level=logging.INFO)

# Метаданные для Alembic
target_metadata = Base.metadata


def run_migrations_online():
    """Run migrations in 'online' mode."""
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        raise ValueError("DATABASE_URL не установлен!")

    print(f"### Используем URL: {db_url}")

    engine = create_engine(db_url)
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    print("### Режим: offline ###")
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True
    )
    with context.begin_transaction():
        context.run_migrations()
else:
    print("### Режим: online ###")
    run_migrations_online()