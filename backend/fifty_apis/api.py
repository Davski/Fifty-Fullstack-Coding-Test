from ninja import NinjaAPI, Schema
from pydantic import EmailStr
from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


api = NinjaAPI()
User = get_user_model()

class RegisterUser(Schema):
    username: str
    password: str
    email: EmailStr

class UserOutput(Schema):
    id: int
    username: str
    email: str

@api.post("/register-user", response={201: UserOutput, 400: dict})
def register_user(request, user: RegisterUser):
    if User.objects.filter(username=user.username).exists():
        return 400, {"detail": "Username is taken"}

    try:
        user = User.objects.create_user(
            username=user.username,
            email=user.email,
            password=user.password,
        )

    except IntegrityError:
        return 400, {"detail": "An Error occured"}
    
    return 201, UserOutput(id=user.id, username=user.username, email=user.email)

class LoginUser(Schema):
    username: str
    password: str
    email: EmailStr

class TokenOutput(Schema):
    access: str
    refresh: str

@api.post("/login-user", response={200: TokenOutput, 401: dict})
def login_user(request, login: LoginUser):
    user = authenticate(
        request,
        username=login.username,
        password=login.password,
    )

    if not user:
        return 401, {"detail": "Invalid username or password"}

    refresh = RefreshToken.for_user(user)
    access = refresh.access_token

    return 200, TokenOutput(access=str(access), refresh=str(refresh))

