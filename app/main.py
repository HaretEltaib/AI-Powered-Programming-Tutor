import uvicorn
from fastapi import FastAPI
from .api.endpoints import api_router

app = FastAPI()
app.include_router(api_router, prefix="/api/v1", tags=["API"])
if __name__ == "__main__":
    uvicorn.run(app="app.main:app", host="localhost", port=8000, reload=True , reload_dirs=['app'])
