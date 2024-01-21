import csv
import json
from time import sleep

from fastapi import FastAPI, Body, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# @app.get("/")
# def root():
#     return FileResponse("/index.html")

with open('binlist-data.csv', 'r') as file:
    bin_db = {info['bin']: info for info in csv.DictReader(file)}


@app.post("/get-info")
async def get_info(data=Body()):
    card_number = data["card_number"].strip()
    if not card_number:
        raise HTTPException(status_code=404, detail="Card number can't be empty")
    try:
        float(card_number)
    except ValueError:
        raise HTTPException(status_code=404, detail="Card number should contain only digits")

    if len(card_number) > 16:
        raise HTTPException(status_code=404, detail="Card number's length can't be greater than 16")

    sleep(3)
    if card_number not in bin_db.keys():
        raise HTTPException(status_code=404, detail="Unknown card")
    return {"data": json.dumps(bin_db[card_number])}


app.mount("/", StaticFiles(directory="html", html=True))
