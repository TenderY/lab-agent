
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.request import LoginRequest
from app.schemas.response import UserResponse
from app.utils.jwt import decode_access_token, encode_access_token
from app.utils.password import hash_password, verify_password
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/user", tags=["用户管理"])

@router.post("/login")
async def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名或密码错误",
        )
    if user.status == 0:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户已被禁用",
        )

    access_token = encode_access_token(user.id)

    return {
        "code": 200,
        "message": "登录成功", 
        "data":
        {
            "access_token": access_token, 
            "user": UserResponse.model_validate(user)
        }
    }


@router.get("/info")
async def get_user_info(user: User = Depends(get_current_user)):
    return {
        "code": 200,
        "message": "获取用户信息成功", 
        "data": UserResponse.model_validate(user)
    }