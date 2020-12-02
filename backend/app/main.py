from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class RoleName(str, Enum):
    admin = "admin"
    assistant = "assistant"
    user = "user"

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


# ================ get items ================
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# ================ get users ================
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# ================ get roles ================
@app.get("/roles/{role_name}")
async def get_model(role_name: RoleName):
    if role_name == RoleName.admin:
        return {"role_name": role_name, "message": "I'm admin. I add, relocate and remove users in/out events and queues."}

    if role_name.value == RoleName.assistant:
        return {"role_name": role_name, "message": "I'm assistant. I help students who enter the queue in an event."}
    
    if role_name.value == RoleName.user:
        return {"role_name": role_name, "message": "I'm user. I want to get lab checkpoint 1 checked off/ask some questions."}

    return {"role_name": role_name, "message": "Whatever. I do what I want."}