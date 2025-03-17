from fastapi import FastAPI

app = FastAPI()

#------------Path Parameters-----------#
# for specific resources
# @app.get("/users/{user_id}")
# def load_user(user_id:int):
#     return {"user": user_id}

# @app.get("/users/{item_name}")
# def load_user(item_name:str):
#     return {"user": item_name} 

#--------------Query Parameter-----------#
"""used to filter or refine the data returned by an end point
   unlike path parameters which are the part of URL structure,
   query parameter appende to the URL after a i d"""
    
# @app.get("/users/")
# def load_user(user_id:int, name:str):
#     return{"user_id":user_id, "name":name}

#optional query parameter name
# @app.get("/users/")
# def load_user(user_id:int, name:str=None):
#     return{"user_id":user_id, "name":name}

#combining path and route parameters?
@app.get("/users/{user_id}/details")
def read_user_details(user_id:int, include_email:bool=False):
    if include_email:
        return {"user_id":user_id, "email":"email included"}
    else:
        return {"user_id":user_id, "email":"email not included"}
