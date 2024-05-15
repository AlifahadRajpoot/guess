from fastapi import FastAPI
import uvicorn
import random
app=FastAPI()
a=random.random()
students=[{
    {"id":a,
    "name":"Ali",
    "age":10,
    "class":1
},    
{
        "id":a,
        "name":"Fahad",
        "age":11,
        "class":2  
    }
}]
@app.get("/students")
def getstudents():
    return students

@app.get("/students/{id}")
def getstdentsid(id):
    print("students id",id)
    return id

@app.post("/addstudent")
def addstudent(id:int,name:str,age:int,classe:int):
    global students
    students.append({"id":id,"name":name,"age":age,"classe":classe})
    return students
    
@app.put("/updatestudent/{id}/{age}")
def updatestudent(id,age):
    students.update({"id":id,"age":age})
    return students

@app.delete("/deletestudent/{id}/{age}")
def deletestudent(id,age):
    students.remove({"id":id,"age":age})
    return students

def start():
    uvicorn.run("fastapi:app",host="127.0.0.1",port=8000)
    








