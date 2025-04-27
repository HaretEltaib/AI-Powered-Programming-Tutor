from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime, timedelta
from jose import jwt

# Initialize the API router
router = APIRouter()

# Secret key and algorithm for JWT encoding
SECRET_KEY = "mysecretkey123"  # Change this to a stronger key in production
ALGORITHM = "HS256"

# Define the request model for login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Function to create a JWT access token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    """
    Generates a JWT access token with an expiration time.

    Args:
        data (dict): The payload data to encode in the token.
        expires_delta (timedelta): The token's expiration time.

    Returns:
        str: Encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Endpoint to handle user login
@router.post("/login")
def login_user(request: LoginRequest):
    """
    Handles user login and returns a JWT token if successful.

    Args:
        request (LoginRequest): The login request containing email and password.

    Returns:
        dict: A response containing the access token and token type.
    """
    # Validate password length
    if len(request.password) < 8:
        raise HTTPException(status_code=400, detail="Password is too short. It must be at least 8 characters.")

    # Normally, you would validate the email and password against a database.
    # For now, we generate a token directly for demonstration purposes.
    token = create_access_token({"sub": request.email})

    return {
        "status": 200,
        "access_token": token,
        "token_type": "bearer"
    }
