from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import math

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/poq')
async def poq():
    return {"message": "HAA PO'O'Q !"}

@app.get("/lcm/roostamovic_yahoo_com", response_class=PlainTextResponse)
async def LCM(x: str, y: str):

    if not x.isdigit() or not y.isdigit():
        return "NaN"
    
    if x == "0" or y == "0":
        return "0"

    x, y = int(x), int(y)
    lcm = x * y
    min_num = min(x, y)
    divs = list(range(math.floor(math.sqrt(min_num)), 1, -1))
    i = 0
    while i < len(divs):
        if x % divs[i] == 0 and y % divs[i] == 0:
            x, y, lcm = int(x / divs[i]), int(y / divs[i]), int(lcm / divs[i])
        else:
            i += 1

    return str(lcm)