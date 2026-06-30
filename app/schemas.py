from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

#What the system receive to be shortend
class URLCreate(BaseModel):
    original_url: HttpUrl #Garantee that is a valid URL
    expires_at: Optional[datetime] = None

#API Response
class URLResponse(BaseModel):
    original_url: str
    short_code: str
    created_at: datetime

    class Config:
        from_attributes =  True #Allow the Pydantic to read all the rights of SQLAlchemy