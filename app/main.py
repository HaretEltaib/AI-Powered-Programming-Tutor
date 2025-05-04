from fastapi import FastAPI
from app.models import users
from app.db.database import engine
from app.api.endpoints import api_router

users.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router, prefix="/api/v1")
