from fastapi import FastAPI
import json 
from pathlib import Path


app = FastAPI()


@app.get("/")
def home():
    return {"message":"running on f** ___er"}


@app.get("/about")
def about():
    return {"message":"building APIs without using the s**t jinja, lets see!!!"}

def load_data():
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "patients.json"
    with open(file_path,"r") as f:
        data = json.load(f)
    return data

@app.get("/view")
def view_records():
    return load_data()