#!/usr/bin/python3
import uuid
from datetime import datetime
"""
the base model from which all models inherent
"""


class BaseModel():
    """
    class with the necessary attributes for all the objects in this project
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """string represebtation to each instance"""
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """each time an instance is modified this function will be called"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        forming the __dict__ into a more likable and readable format
        """
        res_dict = {"__class__": str(__class__.__name__),
                    "updated_at": datetime.isoformat(self.updated_at),
                    "created_at": datetime.isoformat(self.created_at),
                    "id": self.id}
        return res_dict
