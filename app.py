import uvicorn
from fastapi import FastAPI
from fast_micro.user_service.main import user_router

app = FastAPI()

app.include_router(user_router)

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8080)