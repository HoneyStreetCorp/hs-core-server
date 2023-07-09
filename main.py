import uvicorn
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from controller.api import api_router
from core.error import CustomException
from dto.error.error_response import ErrorResponse

app = FastAPI()

# TODO API_PREFIX config file로 분리
app.include_router(api_router, prefix="/api/v1")


@app.get("/ping")
async def pong():
    return "pong"


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.error_response.status_code,
        content=jsonable_encoder(ErrorResponse(message=exc.error_response.message), exclude={"status_code"})
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
