# SQLModel과 alembic 연동(2024-03-06)

## 1. 설치
```
$ pip install sqlmodel alembic
```

## 2. 초기화
```
$ alembic init migrations
```

## 3. alembic.ini 파일 수정
```
sqlalchemy.url = sqlite:///database.db
```
이 부분을
```
# sqlalchemy.url = sqlite:///database.db
```
이렇게 주석 처리를 하고, 사용하지 않는다.

## 4. env.py 파일 수정
```
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import create_engine <-- 구문 추가 -->
from sqlalchemy import pool
import saying_env  # (.env 파일을 읽어올 .py파일)

from models import model  # 모델들을 추가해야 되는지 정확하진 않음

from alembic import context

from sqlmodel import SQLModel <--------------- 구문 추가 --------------->

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# Base = declarative_base()
target_metadata = SQLModel.metadata <--------------- 구문 추가 --------------->

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(saying_env.DATABASE_URL)  <-- 이 부분 수정 -->

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## 5. 실행
```
$ alembic revision --autogenerate -m "commit message"  # 마이그레이션 생성
$ alembic upgrade head  # 마이그레이션 적용
```