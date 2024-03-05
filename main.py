from fastapi import FastAPI
from routers import RestController

app = FastAPI()

app.include_router(RestController.router)