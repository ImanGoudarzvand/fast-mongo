from typing import Any, Dict, List
from bson import ObjectId
from datetime import datetime
from worker import celery

class LoginRepository:
    def __init__(self):
        pass
    

    def insert_login(self, db, details: Dict[str, Any]) -> bool:
        try:
            user = db.find_one({"username": details["username"]})
            if user is None:
                details["timestamp"] = datetime.now()
                db.insert_one(details)
                return True
            else:
                return False

        except Exception as err:
            print(err)

    def delete_login():
        pass 