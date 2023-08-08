from pydantic import BaseModel

class Settings(BaseModel):
    sound_alert: bool
    mobile_alert: bool
