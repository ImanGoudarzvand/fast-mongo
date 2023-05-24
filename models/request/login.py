from pydantic import BaseModel
from typing import List
from datetime import date

class LoginReq(BaseModel): 
    username: str
    password: str 
    