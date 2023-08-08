from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database.models import UserSettingsModel
from .schemas import Settings

class UserSettingsUseCases:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, settings: Settings, user_id: int):
        user_settings_model = UserSettingsModel(settings=settings)
        try:
            self.db_session.add(user_settings_model)
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )

    def update_sound(self, value: bool, user_id: int):
        user_on_db = self.db_session.query(UserSettingsModel).filter_by(user_id=user_id).first()

        if user_on_db is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Invalid user id'
            )
        
        try:
            user_on_db.sound_alert = value
            self.db_session.commit()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Unknown error'
            )
        
        # if not crypt_context.verify(user.password, user_on_db.password):
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail='Invalid username or password'
        #     )
        
        # exp = datetime.utcnow() + timedelta(minutes=expires_in)

        # payload = {
        #     'sub': user.username,
        #     'exp': exp
        # }

        # access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

        # return {
        #     'access_token': access_token,
        #     'exp': exp.isoformat()
        # }