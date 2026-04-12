from models import EmailTriageObservation
from tasks import TASKS
from grader import grade
import random

class EmailTriageEnvironment:
    def __init__(self):
        self.inbox = []
        self.current_email = ""
        self.correct = ""
        self.history = []
        self.step_count = 0
        self.done = False

    def reset(self):
        sample = random.choice(TASKS)

        self.inbox = [sample["email"]]
        self.current_email = sample["email"]
        self.correct = sample["correct"]
        self.history = []
        self.step_count = 0
        self.done = False

        return EmailTriageObservation(
            inbox=self.inbox,
            current_email=self.current_email,
            history=[],
            step_count=0,
            done=False
        )

    def step(self, action):
        self.step_count += 1
        self.history.append(action.action)

        reward = 0.0

        if "classify" in action.action:
            reward = grade(action.action, self.correct, self.step_count)
            self.done = True

        return EmailTriageObservation(
            inbox=self.inbox,
            current_email=self.current_email,
            history=self.history,
            step_count=self.step_count,
            done=self.done
        ), reward, self.done, {
            "correct": self.correct
        }

    def state(self):
        return {
            "email": self.current_email,
            "history": self.history,
            "steps": self.step_count
        }