from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.depends import get_db_session, token_verifier
from .user_settings import UserSettingsUseCases

users_settings_router = APIRouter(prefix='/settings', dependencies=[Depends(token_verifier)])

@users_settings_router.post('/sound/{user_id}')
def set_sound(
    user_id: int,
    value: bool,
    db_session: Session = Depends(get_db_session)
):
    use_case = UserSettingsUseCases(db_session=db_session)
    use_case.update_sound(value=value, user_id=user_id)
