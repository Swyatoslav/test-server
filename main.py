import csv
import json
from time import sleep

from fastapi import FastAPI, Body, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

with open('binlist-data.csv', 'r') as file:
    bin_db = {info['bin']: info for info in csv.DictReader(file)}


@app.post("/get-info")
async def get_info(data=Body()):
    raw_card_number = data["card_number"]
    if not raw_card_number:
        raise HTTPException(status_code=400, detail="Card number can't be empty")
    if not isinstance(raw_card_number, str):
        raise HTTPException(status_code=400, detail="Card number should be string")
    card_number = raw_card_number.strip()
    try:
        float(card_number)
    except ValueError:
        raise HTTPException(status_code=400, detail="Card number should contain only digits")

    if len(card_number) > 16:
        raise HTTPException(status_code=400, detail="Card number's length can't be greater than 16")

    sleep(3)
    if card_number not in bin_db.keys():
        raise HTTPException(status_code=404, detail="Unknown card")
    return {"data": json.dumps(bin_db[card_number])}


app.mount("/", StaticFiles(directory="html", html=True))
