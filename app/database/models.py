from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from app.database.base import Base
from .connection import engine

class UserModel(Base):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)

    settings = relationship("UserSettingsModel", back_populates="user", uselist=False)

class UserSettingsModel(Base):
    __tablename__ = 'users_settings'

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    sound_alert = Column('sound_alert', Boolean, default=True)
    mobile_alert = Column('mobile_alert', Boolean, default=True)

    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship("UserModel", back_populates="settings")
    

Base.metadata.create_all(bind=engine)