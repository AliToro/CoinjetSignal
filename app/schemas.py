from typing import List, Union

from pydantic import BaseModel


class SignalBase(BaseModel):
    email: str


class SignalCreate(SignalBase):
    password: str


class Signal(SignalBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
