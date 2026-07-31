from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv() # tells python to open .env file read the variables and place them in application env
# DATABASE_URL = "mysql+pymysql://root:Abdulla#12@localhost:3306/e_commerce"
DATABASE_URL = os.getenv("Db_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



