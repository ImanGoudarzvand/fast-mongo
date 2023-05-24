from celery import Celery 


celery = Celery(__name__)
celery.conf.broker_url = "redis://localhost:6379"
celery.conf.result_backend = "redis://localhost:6379"


@celery.task(name="say_goodbuy")
def say_goodbuy():
    print("goodbuy")

from db_config.pymongo import create_db_collections

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
# try:
db = client.obrs
buyers = db.buyer
users = db.login

@celery.task(name="task_add_login")
def task_add_login(data):

    # rep.insert_login(db["users"], details)
    # print(details)
    # db.insert_one(details)
    # login_dict = req.dict()
    print(data)
    print(users.insert_one(data))
    # print(db)
    # a = db["users"]
    # a.insert_one(data)
    # collection.insert_one(data)
    print("task done")

@celery.task(name="task_show_records")
def task_show_records():

    # rep.insert_login(db["users"], details)
    # print(details)
    # db.insert_one(details)
    # login_dict = req.dict()
    # print(data)
    # print(users.insert_one(data))
    # print(db)
    logins = users.find()
    # a = db["users"]
    # a.insert_one(data)
    # collection.insert_one(data)
    print(logins)
    print("task done")
    return logins



