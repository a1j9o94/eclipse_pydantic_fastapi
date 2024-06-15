from pydantic import BaseModel, Field
import uuid

class ReputationTile(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    points: int

