from fastapi import FastAPI
import os
import uvicorn
from dotenv import load_dotenv
from routers.houses import router as house_router
from routers.locations import router as location_router
from contextlib import asynccontextmanager
from db.engine import init_db, close_db


abstr_file_path = os.path.abspath(__file__)
curr_file_path = os.path.dirname(abstr_file_path)
dotenv_path = os.path.join(os.path.dirname(curr_file_path), '.env')
load_dotenv(dotenv_path)

@asynccontextmanager
async def app_lifespan(app : FastAPI):
    # pass
    await init_db()
    # yield
    # await close_db()

app = FastAPI()

app.include_router(house_router)
app.include_router(location_router)

HOUSE_API_APP_HOST = os.environ.get('HOUSE_API_APP_HOST')
HOUSE_API_APP_PORT = os.environ.get('HOUSE_API_APP_PORT')

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000
    )
