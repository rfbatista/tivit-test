from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import pbkdf2_sha256

from app.infrastructure.database.database import get_user, fake_users_db
from app.infrastructure.config.config import app_config


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pbkdf2_sha256.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    user = get_user(fake_users_db, username)
    if not user or not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    expire_time = app_config.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    if expire_time is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="missing expiration time",
        )
    expire = datetime.utcnow() + (
        expires_delta if expires_delta else timedelta(minutes=int(expire_time))
    )
    data.update({"exp": expire})
    return jwt.encode(
        data,
        app_config.get("SECRET_KEY") or "",
        algorithm=app_config.get("ALGORITHM") or "",
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            app_config.get("SECRET_KEY") or "",
            algorithms=[app_config.get("ALGORITHM") or ""],
        )
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        return get_user(fake_users_db, username)
    except JWTError:
        raise credentials_exception
