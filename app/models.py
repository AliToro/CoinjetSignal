from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, TIMESTAMP, ARRAY
from sqlalchemy.orm import relationship

from .database import Base


class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Integer)
    full_text = Column(String)
    telegram_chat_id = Column(String)
    telegram_chat_title = Column(String)
    pair = Column(String)
    stop = Column(Float)
    entry = Column(ARRAY(Float))  # (array of entries)
    target = Column(Float)  # (array of TPs)
    is_futures = Column(Boolean)
    is_short = Column(Boolean)  # (required if is_futures)
    leverage = Column(Float)  # (required if is_futures)
    received_at = Column(TIMESTAMP)
    delivered_at = Column(TIMESTAMP)
