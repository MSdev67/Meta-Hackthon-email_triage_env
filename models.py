from pydantic import BaseModel
from typing import List

class EmailTriageObservation(BaseModel):
    inbox: List[str]
    current_email: str
    history: List[str]
    step_count: int
    done: bool

class EmailTriageAction(BaseModel):
    action: str  # classify:spam / summarize / reply / next