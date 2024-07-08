from pydantic import BaseModel
from typing import Optional

class Create_User(BaseModel):
    id : int
    name : str
    email: Optional[str] = None