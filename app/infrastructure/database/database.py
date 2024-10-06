from app.infrastructure.database.models import UserInDB
from passlib.hash import pbkdf2_sha256

fake_users_db = {
    "user": {
        "username": "user",
        "role": "user",
        "password": pbkdf2_sha256.hash("L0XuwPOdS5U"),
    },  # senha: L0XuwPOdS5U
    "admin": {
        "username": "admin",
        "role": "admin",
        "password": pbkdf2_sha256.hash("JKSipm0YH"),
    },  # senha: JKSipm0YH
}


def get_user(db, username: str):
    user = db.get(username)
    if user:
        return UserInDB(**user)
