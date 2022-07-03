from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, DATETIME
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
    entry = Column(Float)  # (array of entries)
    target = Column(Float)  # (array of TPs)
    is_futures = Column(Boolean)
    is_short = Column(Boolean)  # (required if is_futures)
    leverage = Column(Float)  # (required if is_futures)
    received_at = Column(DATETIME)
    delivered_at = Column(DATETIME)
