from fastapi import FastAPI
import json
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/meteo")
def read_meteo():
    with open ("data.json", "r") as file:
        data = json.load(file)
    return data
