from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.users.auth_user import UserUseCases
from .schemas import UserInDB

user_router = APIRouter(prefix='/user')

@user_router.post('/register')
def user_register(
    user: UserInDB,
    db_session: Session = Depends(get_db_session),
):
    use_case = UserUseCases(db_session=db_session)
    use_case.user_register(user=user)
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_201_CREATED
    )

@user_router.post('/login')
def user_login(
    request_form_user: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session),
):
    use_case = UserUseCases(db_session=db_session)
    user = UserInDB(
        username=request_form_user.username,
        password=request_form_user.password
    )

    auth_data = use_case.user_login(user=user)
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )
