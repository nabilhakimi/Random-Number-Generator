from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.get("/random/")
def get_random_number(lower_limit: int, upper_limit: int):
    if lower_limit < 0:
        raise HTTPException(status_code=400, detail="Lower limit must be non-negative.")
    if lower_limit > upper_limit:
        raise HTTPException(status_code=400, detail="Lower limit cannot exceed upper limit.")

    number = random.randint(lower_limit, upper_limit)
    return {"random_number": number}
