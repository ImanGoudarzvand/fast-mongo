from fastapi import APIRouter, Depends
from db_config.pymongo import create_db_collections
from models.request.login import LoginReq
from repository.login import LoginRepository
# from tasks import say_hello
router = APIRouter()


@router.post("/login")
def add_login(req: LoginReq, db = Depends(create_db_collections), login_service = Depends(LoginRepository)):

    login_dict = req.dict(exclude_unset = True)
    print(login_service.insert_login(db["users"], login_dict))
    


