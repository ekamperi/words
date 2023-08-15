from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import random

app = FastAPI()


with open('p.txt') as f:
    p_words = [x.rstrip() for x in f] # remove line breaks

with open('h.txt') as f:
    h_words = [x.rstrip() for x in f] # remove line breaks

with open('d.txt') as f:
    d_words = [x.rstrip() for x in f] # remove line breaks

@app.get("/")
def read_root():
    p_idx = random.randrange(0, len(p_words))
    h_idx = random.randrange(0, len(h_words))
    d_idx = random.randrange(0, len(d_words))
    phd = p_words[p_idx] + " " + h_words[h_idx] + " " + d_words[d_idx]

    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>PhD meme generator</title>
        </head>
        <body style="background-color: #a2bfe04d;">
            <h1 style="font-family: sans-serif; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; min-height: 70vh;">PhD is {phd}</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
