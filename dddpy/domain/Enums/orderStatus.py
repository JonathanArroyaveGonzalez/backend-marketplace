from enum import Enum

class orderStatus(int, Enum):
    CREATED = 0,
    CANCELLED = 1,
    DELIVERED = 2