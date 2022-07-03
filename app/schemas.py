from typing import List, Union, Optional

from pydantic import BaseModel
from datetime import datetime


class SignalBase(BaseModel):
    full_text: str
    telegram_chat_id: str
    telegram_chat_title: str
    pair: str
    stop: float
    entry: float  # (array of entries)
    target: float  # (array of TPs)
    is_futures: bool
    is_short: bool  # (required if is_futures)
    leverage: Optional[float] # (required if is_futures)


class SignalCreate(SignalBase):
    received_at: datetime


class Signal(SignalBase):
    id: int
    received_at: datetime
    sent_at: datetime
    status: int

    class Config:
        orm_mode = True
