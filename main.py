import csv
import json
from time import sleep

from fastapi import FastAPI, Body, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

with open('binlist-data.csv', 'r') as file:
    bin_db = {info['bin']: info for info in csv.DictReader(file)}


@app.get("/ping")
async def ping():
    return 'pong'


@app.post("/get-info")
async def get_info(data=Body()):
    if not data:
        raise HTTPException(status_code=400, detail="Empty request body")
    if not data.get('bin_number'):
        raise HTTPException(status_code=400, detail="No 'bin_number' field in request")
    raw_bin_number = data["bin_number"]
    if not raw_bin_number:
        raise HTTPException(status_code=400, detail="BIN number can't be empty")
    if not isinstance(raw_bin_number, str):
        raise HTTPException(status_code=400, detail="BIN number should be string")
    bin_number = raw_bin_number.strip()
    try:
        float(bin_number)
    except ValueError:
        raise HTTPException(status_code=400, detail="BIN number should contain only digits")

    if len(bin_number) < 5:
        raise HTTPException(status_code=400, detail="BIN number's length can't be less than 5")

    if len(bin_number) > 16:
        raise HTTPException(status_code=400, detail="BIN number's length can't be greater than 16")

    sleep(3)
    if bin_number not in bin_db.keys():
        raise HTTPException(status_code=404, detail="Unknown BIN")
    return {"data": bin_db[bin_number]}


app.mount("/", StaticFiles(directory="html", html=True))
