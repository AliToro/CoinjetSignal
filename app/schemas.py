from typing import List, Union, Optional

from pydantic import BaseModel
from datetime import datetime


class SignalBase(BaseModel):
    full_text: str
    telegram_chat_id: str
    telegram_chat_title: str
    pair: str
    stop: Optional[float]
    entry: Optional[float]  # (array of entries)
    target: Optional[float]  # (array of TPs)
    is_futures: Optional[bool]
    is_short: Optional[bool]  # (required if is_futures)
    leverage: Optional[float] # (required if is_futures)
    received_at: Optional[datetime]
    delivered_at: Optional[datetime]
    status: Optional[int]


class SignalCreate(SignalBase):
    pass


class Signal(SignalBase):
    id: int

    class Config:
        orm_mode = True
