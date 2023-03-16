from typing import Optional
from pydantic import BaseModel
import datetime

class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int 
    complete: bool
    owner_id: int



class Read(BaseModel):
        class Config:
            orm_mode = True

class Create(BaseModel):
        class Config:
            orm_mode = True

class Patch(BaseModel):
        nickname: Optional[str] 
        class Config:
            orm_mode = True

