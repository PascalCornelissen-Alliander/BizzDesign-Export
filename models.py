from pydantic import BaseModel

class Term(BaseModel):
    name: str
    definition: str
    register: str