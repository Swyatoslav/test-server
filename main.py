import csv

from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import json
from time import sleep

app = FastAPI()

# @app.get("/")
# def root():
#     return FileResponse("/index.html")

with open('binlist-data.csv', 'r') as file:
    bin_db = {info['bin']: info for info in csv.DictReader(file)}


@app.post("/get-info")
async def root(data=Body()):
    card_number = data["card_number"].strip()
    if not card_number:
        raise HTTPException(status_code=404, detail="Card number can't be empty")
    try:
        float(card_number)
    except ValueError:
        raise HTTPException(status_code=404, detail="Card number should contain only digits")

    sleep(3)
    if card_number not in bin_db.keys():
        raise HTTPException(status_code=404, detail="Unknown card")
    return {"data": json.dumps(bin_db[card_number])}


app.mount("/", StaticFiles(directory="html", html=True))