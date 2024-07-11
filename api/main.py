from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

@app.get("/")
def read_data():
    
    return {"Status": "Ok"} 


@app.get("/data")
def read_data():
    with open('../scrapeme/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
