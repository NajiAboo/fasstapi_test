from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

app = FastAPI()

user_db ={
    1: {"name": "naji", "age": 20},
    2: {"name": "aboo", "age":74},
    3: {"name": "fath", "age": 60}
}


@app.put("/user/{user_id}")
def user_update(user_id: int, user_data: User):
    if user_id in user_db:
        user_db[user_id] = user_data.model_dump()
        return {"message": "user updated successfull", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}
    

@app.get("/user")
def user_details():
    return user_db
    

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
    else:
        return {"message": "no record found"}

    return {"message" : "sucessfully deleted the uer"}