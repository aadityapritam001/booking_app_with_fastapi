from pydantic import BaseModel
from typing import Optional
import uuid



class Center(BaseModel):
    id : Optional[uuid.UUID] = uuid.uuid4()
    name : str
    location: str
    description: Optional[str] = None
    amenities: list
    timing: str
    is_occupied: bool

    class Config:
        from_attributes=True