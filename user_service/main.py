import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter,status,HTTPException
from fast_micro.user_service.model import User
from fast_micro.user_service.schema import Create_User

app = FastAPI()
user_router = APIRouter(prefix='/user_service')

data = []

@user_router.post('/create_user')
async def create_user(user:Create_User):
    new_user = User(id = user.id,name = user.name,email = user.email)
    data.append(new_user)
    return new_user

@user_router.get('/get_users')
async def get_user():
    return data

@user_router.put('/update_user/{num}')
async def update_user(num:int,updated_user:Create_User):
    for item in data:
        if item.id == num:
            item.name = updated_user.name
            item.email = updated_user.email
            print(item)
            return item
    raise HTTPException(status_code=404,detail='id not found !')


