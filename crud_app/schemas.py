from pydantic import BaseModel, validator
from datetime import date
from fastapi import HTTPException
from uuid import UUID
from typing import Optional

class UserCreate(BaseModel):
    user_name: str
    password: str
    

    @validator("password")
    def validate_password_strength(cls, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isalpha() for char in password):
            raise ValueError("Password must contain at least one letter")
        
        return password



class Userlogin(BaseModel):
    user_name: str
    password: str



class Transaction_Schema(BaseModel):
    amount : float
    description :str


