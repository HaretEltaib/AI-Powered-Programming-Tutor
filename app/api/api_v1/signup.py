from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, ValidationError
import re

router = APIRouter()

class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

def validate_name(name: str):
    if any(char.isdigit() for char in name):
        raise HTTPException(status_code=400, detail="❌ الاسم لا يجب أن يحتوي على أرقام.")
    if len(name.strip()) < 2:
        raise HTTPException(status_code=400, detail="❌ الاسم قصير جدًا.")

def validate_password(password: str):
    if len(password) < 8:
        raise HTTPException(status_code=400, detail="❌ كلمة السر يجب أن تكون 8 حروف أو أكثر.")
    if not re.search(r"[A-Za-z]", password) or not re.search(r"[0-9]", password):
        raise HTTPException(status_code=400, detail="❌ كلمة السر يجب أن تحتوي على حروف وأرقام.")

@router.post("/signup")
def signup_user(request: SignupRequest):
    try:
        validate_name(request.name)
        validate_password(request.password)
    except HTTPException as e:
        raise e
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"❌ خطأ في البيانات المدخلة: {e}")

    return {
        "status": 201,
        "message": f"✅ تم إنشاء الحساب بنجاح: {request.name}."
    }
