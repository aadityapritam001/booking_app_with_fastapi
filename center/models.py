from sqlalchemy import Column, String, Boolean, UUID, ARRAY
import uuid
from database.db import  Base
from sqlalchemy import inspect

class Center(Base):
    __tablename__ = "centers"

    id = Column(UUID, primary_key = True)
    name = Column(String, nullable= False)
    location = Column(String, nullable = False)
    description = Column(String, nullable = True)
    amenities = Column(ARRAY(String), nullable = False)
    timing = Column(String, nullable = False)
    is_occupied = Column(Boolean, default= False)


    def to_dict(self) -> dict:
        """Convert the model to a dictionary.

        :return: Dictionary of the model
        :rtype: dict
        """
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

