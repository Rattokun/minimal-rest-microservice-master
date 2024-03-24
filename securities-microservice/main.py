from __future__ import annotations

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests
import random
import uvicorn
import os
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def root_to_json(token):
    data = {'token': token}
    data = json.dumps(data)  # dict to string
    data = json.loads(data)  # string to json
    print
    data['Processes']

@app.get("/")
async def root():
    r = root_to_json("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJ1c2VyX2lkIjoxLCJlbWFpbCI6Im1pa2UucGF5bmVAZXhhbXBsZS5jb20iLCJpYXQiOjE3MTA2ODYxOTAsImV4cCI6MTcxMDY4OTc5MH0.O8dsdrzcXIwsuhO_OXi_QCxCiMm-XzVDuOJhGyKzLVY")
    return r



@app.get("/list/")
async def get_list():
    film_list = []

    r = requests.get(f"trefle.io/api/v1/species",
                     headers={'Authorization': '_nWoT7ek3RMYpCvaSLfrE3S1BWXblk1df3IeA2ww064'})
    film_list.append(r.json())
    return film_list


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT', 80)))
