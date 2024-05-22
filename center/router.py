from fastapi import APIRouter, Depends
import asyncio
from center import schema
from database.db import Database
from center import services


center_app = APIRouter()
session= asyncio.run(Database.get_db())
db = session()

@center_app.post("/create", )
async def create_center(center_details: schema.Center):
    return await services.add_center(db,center_details) 


