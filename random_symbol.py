from fastapi import FastAPI
from random import choice

app = FastAPI()

@app.get("/random_letter")
async def read_random_letter():
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ`~!@#$%^&*()_+-=[]\;',./{}|:\"<>"
    random_letter = choice(alphabet)
    return {"letter": random_letter}