from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
    sender: str
    recipient: str
    content: str
    timestamp: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "sender": "user1",
                "recipient": "user2",
                "content": "Hello, how are you?",
                "timestamp": "2024-02-09T12:00:00"
            }
        }
