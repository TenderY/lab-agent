from datetime import datetime, timedelta

import jwt
from app.config import settings
from fastapi import HTTPException


def encode_access_token(user_id: int):
    """创建JWT token"""
    expire_time = datetime.now() + timedelta(hours=settings.JWT_EXPIRE_HOURS)
    payload = {
        "user_id": user_id,
        "exp": expire_time
    }

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def decode_access_token(token: str)->dict:
    """解码JWT token"""
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token已过期")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token无效")