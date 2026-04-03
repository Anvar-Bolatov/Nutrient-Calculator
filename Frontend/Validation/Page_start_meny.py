from pydantic import BaseModel


class ValidationStartMenu(BaseModel):
    product : str
    mass : str
    number : int

