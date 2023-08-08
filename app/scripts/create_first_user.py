from fastapi import HTTPException
from app.database.models import UserModel
from app.users.auth_user import UserUseCases
from app.users.schemas import UserInDB
from fastapi import status
from app.database.connection import Session
from dotenv import load_dotenv
from os import getenv
load_dotenv()

username = getenv("FIRST_ADMIN_USERNAME")
password = getenv("FIRST_ADMIN_PASSWORD")

def create_first_admin():
    db_session = Session()

    user = UserInDB(username=username, password=password)
    user_use_case = UserUseCases(db_session=db_session)
    user_on_db = user_use_case.db_session.query(UserModel).filter_by(username=user.username).first()

    if user_on_db is None:
        user_use_case.user_register(user=user)

    db_session.close()
