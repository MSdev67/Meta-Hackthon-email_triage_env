from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    action: str

state = {"email": "", "done": False}

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    state["email"] = "Test email"
    state["done"] = False
    return state

@app.post("/step")
def step(action: Action):
    reward = 1.0 if "important" in action.action.lower() else 0.0
    state["done"] = True

    return {
        "observation": state,
        "reward": reward,
        "done": True,
        "info": {}
    }