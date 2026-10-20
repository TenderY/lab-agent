from app.database import get_db
from app.models.user import User
from app.utils.jwt import decode_access_token
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login", scheme_name="JWT")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db))->User:
    """获取当前用户"""
    try:
        payload = decode_access_token(token)
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token无效")
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")
        if user.status == 0:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="用户已被禁用")
        return user
        
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token无效") from e
