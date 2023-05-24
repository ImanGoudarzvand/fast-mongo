from fastapi import FastAPI, Depends
from typing import Dict
from api.login import router as loginRouter
from db_config.pymongo import create_db_collections
from repository.login import LoginRepository
from models.request.login import LoginReq

app = FastAPI()

# app.include_router(loginRouter, prefix="/api")


# from worker import say_goodbuy
from worker import say_goodbuy, task_add_login

@app.get("/tasks")
def trigger_task():
    task = say_goodbuy.delay()
    return {"message": task.id}



@app.post("/login-task")
def add_login(req: LoginReq, db = Depends(create_db_collections)):

    data = req.dict()
    task_add_login.delay(data=data)
    return {"ok"}

from worker import task_show_records 

@app.get("/login-task")
def get_logins():

    # data = req.dict()
    task_show_records.delay()

    return {"ok"}

