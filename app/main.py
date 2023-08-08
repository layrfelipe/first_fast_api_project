from fastapi import FastAPI
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.users.router import user_router
from app.user_settings.router import users_settings_router
from app.scripts.create_first_user import create_first_admin

app = FastAPI()

@app.get('/')
def health_check():
    return "Ok, it's working"

app.include_router(user_router)
app.include_router(users_settings_router)

create_first_admin()