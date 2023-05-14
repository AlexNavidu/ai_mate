# Проект Ai_Mate

## Использованные технологии и пакеты 
* [FastAPI](https://fastapi.tiangolo.com/) 
* [FastAPI Users](https://fastapi-users.github.io/fastapi-users/10.1/) 
* [SQLAlchemy](https://www.sqlalchemy.org/) 
* [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) 
* [Docker](https://www.docker.com)

## Необходимый софт 
Для развертывания проекта локально, на Вашем комьютере требуется:
- Python вресии 3.9 и выше. <br>
- docker <br>

---
### Запуск проекта. 

#### 1. Шаг клонировать репозиторий. 

`git clone git@github.com:AlexNavidu/ai_mate.git`

#### 2. Создать файл .env в корне проекта. 

Шаблон заполнения файла. 

`DATABASE_URL = postgresql+asyncpg://POSTGRES_USER:POSTGRES_PASSWORD@NAME_CONTAINER_POSTGRESS:5432/POSTGRES_DB

POSTGRES_USER=user <br>
POSTGRES_PASSWORD=passsword <br>
POSTGRES_DB=database_ai_mate <br>
DB_HOST=0.0.0.0 <br>
DB_PORT=5432 <br>` 

SECRET = add some word


#### 3. В корне проекта запустить

docker-compose up --build

---

#### Работа с api 
Документация ко всем ручкам описана в http://127.0.0.1/docs
