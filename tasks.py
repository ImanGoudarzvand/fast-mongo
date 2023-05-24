from .worker import celery
# from repository.login import LoginRepository
from typing import Dict, Any

@celery.task
def say_goodbuy():
    print("goodbuy")


# @celery.task(name="insert_login_task")
# def insert_login_task(rep: LoginRepository, db, details: Dict[str, Any]):
#     rep.insert_login(db, details)
