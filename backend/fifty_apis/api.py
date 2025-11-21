from datetime import datetime
from ninja import NinjaAPI, Schema
from pydantic import EmailStr, constr
from django.contrib.auth import authenticate, get_user_model
from django.db import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Reading


api = NinjaAPI()
User = get_user_model()

class RegisterUser(Schema):
    username: constr(strip_whitespace=True, min_length=3)
    password: constr(strip_whitespace=True, min_length=6)
    email: EmailStr

class UserOutput(Schema):
    username: str
    email: str

@api.post('/register-user', response={201: UserOutput, 400: dict})
def register_user(request, user: RegisterUser):
    """
    Registers a user

    **Input**:

    - **username**: Name - minimum length 3 character
    - **password**: Password - minimum length 6 characters
    - **email**: Email - Should be unique with correct formatting

    **Response**: 201 Created: Body contains the username and email
    """

    if User.objects.filter(username=user.username).exists():
        return 400, {'detail': 'Username is taken'}

    user = User.objects.create_user(
            username=user.username,
            email=user.email,
            password=user.password,
        )

    return 201, UserOutput(username=user.username, email=user.email)

class LoginUser(Schema):
    username: str
    password: str

class TokenOutput(Schema):
    access: str
    refresh: str

@api.post('/login-user', response={200: TokenOutput, 400: dict})
def login_user(request, login: LoginUser):
    """
    Logs a user in

    **Input**:

    - **username**: Name - minimum length 3 character
    - **password**: Password - minimum length 6 characters

    **Response**: 200 OK: Body contains refresh and access tokens
    """

    user = authenticate(
        request,
        username=login.username,
        password=login.password,
    )

    if not user:
        return 400, {'detail': 'Invalid username or password'}

    refresh = RefreshToken.for_user(user)
    access = refresh.access_token

    return 200, TokenOutput(access=str(access), refresh=str(refresh))

class readingOutput(Schema):
    sensor: str
    temperature: float
    humidity: float
    timestamp: datetime

@api.get('/readings', response={200: list[readingOutput], 404: dict})
def get_readings(request):
    """
    Gets all readings

    **Response**: 200 OK: Returns full list of readings

    """

    reading_list = list(Reading.objects.values('sensor', 'temperature', 'humidity', 'timestamp'))
    if not reading_list:
        return 404, {'detail': 'Database is empty'}
    return 200, reading_list
