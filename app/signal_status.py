from enum import Enum


class SignalStatus(Enum):
    Received = 1
    Retry = 2
    Delivered = 3
    Failed = 4
