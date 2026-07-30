from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:Abdulla#12@localhost:3306/e_commerce"
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_PTpeXOdNtfJlyuxfzgy@mysql-587eb8b-skabdulla346-4689.c.aivencloud.com:15304/defaultdb"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



