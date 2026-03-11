from pydantic import BaseModel,model_validator,field_validator
from typing import Literal
from Core.settings import TYPE_KG,TYPE_GRAMM

class Validate_Console(BaseModel):
    product : str
    mass : Literal[f'{TYPE_GRAMM}',f'{TYPE_KG}']
    number : int
    text : str = None

    @model_validator(mode='after')
    def transform_text(self):
        self.text = f'{self.number}{self.mass} {self.product}'
        return self