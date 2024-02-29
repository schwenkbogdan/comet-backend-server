from fastapi import APIRouter, Depends
from .models import Message
from .database import get_database

router = APIRouter()

@router.post("/messages/", response_model=Message, status_code=201)
async def send_message(message: Message, db=Depends(get_database)):
    # Сохраните сообщение в базе данных
    # Здесь должна быть логика сохранения сообщения в MongoDB
    return message

@router.get("/messages/{recipient}", response_model=list[Message])
async def get_messages(recipient: str, db=Depends(get_database)):
    # Получите все сообщения для указанного получателя из базы данных
    # Здесь должна быть логика получения сообщений из MongoDB
    return []
