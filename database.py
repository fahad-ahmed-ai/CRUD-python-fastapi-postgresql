from sqlalchemy import NullPool, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config


DATABASE_URL = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    config("DB_USER"), config("DB_PASSWORD"), config("DB_HOST"), config("DB_PORT"), config("DB_NAME"), poolclass=NullPool
)

print(DATABASE_URL)

db_engine = create_engine(
    DATABASE_URL,
    pool_size=30,
    max_overflow=15,
    pool_pre_ping=True,
    pool_recycle=60 * 60,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine, future=True)

Base = declarative_base()
