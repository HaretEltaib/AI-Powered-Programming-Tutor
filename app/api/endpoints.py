from fastapi import APIRouter
from .api_v1 import login, signup,health

api_router = APIRouter()


# router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(login.router, prefix="/users", tags=["Login"])
api_router.include_router(signup.router, prefix="/users", tags=["Signup"])
