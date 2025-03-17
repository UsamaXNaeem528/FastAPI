#-------------Request and response bodies-----------------#

#handling request
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

@app.post("/users/")
async def create_user(user:User):
    return {"sended user" : user.name, "sended age":user.age}

#handling response
@app.get("/users/{user_id}",response_model=User)
async def get_user(user_id:int):
    return {"name":"usama", "age":18}