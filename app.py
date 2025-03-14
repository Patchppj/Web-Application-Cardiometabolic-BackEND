from typing import Union
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

#http://127.0.0.1:8000/get-message?name=Patch
@app.get("/get-message")
def hello(name: str):
    return {"Message": f"Congrats {name}! This is your first API!"}

# Initial static string
static_string = "Initial Text"

@app.post("/add")
async def add_text(text: str):
    global static_string
    static_string += text
    return {"message": "Text added", "current_string": static_string}

@app.put("/change")
async def change_text(new_text: str):
    global static_string
    static_string = new_text
    return {"message": "Text changed", "current_string": static_string}

@app.delete("/remove")
async def remove_text():
    global static_string
    static_string = ""
    return {"message": "Text removed"}

if name == "main":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")