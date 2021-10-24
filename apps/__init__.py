import os
import uvicorn
from typing import Optional
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import motor.motor_asyncio
import re
app = FastAPI()

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.app_db

# routers
from apps.play import play

app.include_router(play, prefix = '/api/play')