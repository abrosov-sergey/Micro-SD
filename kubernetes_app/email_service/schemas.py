from uuid import UUID

from pydantic import BaseModel


class NewStatusSchema(BaseModel):
    session_id: UUID
    email: str
    new_status_id: int
