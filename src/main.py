from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from databases import Database
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

# Получите переменные окружения
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Добавляем CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы из любых источников
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Создание экземпляра приложения FastAPI app = FastAPI()

# Настройки подключения к базе данных

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Инициализация базы данных
database = Database(DATABASE_URL)
metadata = MetaData()

# Определение таблицы пользователей
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("username", String, unique=True, index=True),
    Column("email", String, unique=True, index=True),
    Column("password", String),
)

# Создание таблицы, если её нет
@app.on_event("startup")
async def startup():
    await database.connect()
    engine = create_engine(DATABASE_URL)
    metadata.create_all(engine)

# Модель для приема данных от клиента
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Создание нового пользователя
@app.post("/users/")
async def create_user(user: UserCreate):
    query = users.insert().values(
        username=user.username,
        email=user.email,
        password=user.password
    )
    await database.execute(query)
    return {"message": "User created successfully"}
