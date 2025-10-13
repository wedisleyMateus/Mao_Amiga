from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

engine = create_async_engine(settings.DATABASE_URL)
async_session  = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = async_session()
    try:
        yield db
    finally:
        db.close()
