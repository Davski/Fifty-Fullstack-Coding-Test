from typing import Optional
from ninja import NinjaAPI, Schema
from pydantic import EmailStr

api = NinjaAPI()

class RegisterUser(Schema):
    name: str
    password: str
    email: Optional[EmailStr] = None
    
@api.post("/register-user")
def register_user(request, User: RegisterUser):
    return {"username": User.name, "password": User.password, "email": User.email}


