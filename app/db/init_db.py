from .base import Base
from .session import engine

import app.models  # needed to register models

def init_db():
    Base.metadata.create_all(bind=engine)