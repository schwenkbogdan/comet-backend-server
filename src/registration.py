# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databases import Database
from dotenv import load_dotenv
import os
from registration import register_user  # Импортируем метод register_user из файла registration.py

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

# Создание таблицы, если её нет
@app.on_event("startup")
async def startup():
    await database.connect()

# Модель для приема данных от клиента
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Создание нового пользователя
@app.post("/users/")
async def create_user(user: UserCreate):
    return await register_user(database, user.dict())  # Вызываем метод register_user из registration.py