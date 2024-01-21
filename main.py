import csv

from fastapi import FastAPI, Body
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
    card_number = data["card_number"]
    sleep(3)
    return {"data": json.dumps(bin_db[card_number])}


app.mount("/", StaticFiles(directory="html", html=True))