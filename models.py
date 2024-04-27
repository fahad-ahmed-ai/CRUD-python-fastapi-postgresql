from sqlalchemy import Integer, String, Column,Boolean,\
    DateTime, Float
from database import Base
from datetime import datetime
from Utilities.config import TIME_ZONE
import pytz as pytz
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func

class BaseModel(Base):
    __abstract__ = True
    created_on = Column(DateTime, default=datetime.now(pytz.timezone(TIME_ZONE)))
    updated_on = Column(DateTime, default=datetime.now(pytz.timezone(TIME_ZONE)),\
                        nullable=True)
    is_active = Column(Boolean, default=True)

class User(Base):
    __tablename__ = "user_cred"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    amount = Column(Float, index=True)
    description = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(String, index=True)