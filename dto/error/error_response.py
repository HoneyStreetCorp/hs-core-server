from typing import Optional

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    message: str
    status_code: Optional[int] = None
