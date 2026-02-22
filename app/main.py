from fastapi import FastAPI
from contextlib import asynccontextmanager
import app.db.init_db as db

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.init_db()
    yield
    # Perform any necessary cleanup here

app = FastAPI(title="SentinelSim", lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

