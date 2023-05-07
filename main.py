import uvicorn
from fastapi import FastAPI

from controller.api import api_router

app = FastAPI()

# TODO API_PREFIX config file로 분리
app.include_router(api_router, prefix="/api/v1")


@app.get("/ping")
async def pong():
    return "pong"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
