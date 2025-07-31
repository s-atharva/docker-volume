from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_json():
    with open('data/mydata.json', 'r') as f:
        print("Reading from path: /data/mydata.json")
        data = json.load(f)
    return data
