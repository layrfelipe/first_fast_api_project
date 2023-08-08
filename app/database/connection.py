from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv
load_dotenv()

DB_URL = getenv('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)