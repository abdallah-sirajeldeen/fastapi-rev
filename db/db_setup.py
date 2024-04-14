from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://fast:fast@localhost/fast_lms"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True  # future=True allows us to use the new Async API
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()


# db utility
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()