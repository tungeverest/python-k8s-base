import logging
from os import getenv
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

db_engine = create_engine(
    url=getenv("SQLALCHEMY_DATABASE_URL"),
    # echo=getenv("DB_ECHO"),
    future=True,
)


LocalSession = sessionmaker(
    bind=db_engine,
    expire_on_commit=False, autocommit=False, autoflush=False,
)


@contextmanager
def get_db():
    with LocalSession() as db_session:
        try:
            logger.debug("DONE")
            yield db_session
        except Exception:
            #  rollback the db session if any exception occurs
            db_session.rollback()
        finally:
            db_session.close()
