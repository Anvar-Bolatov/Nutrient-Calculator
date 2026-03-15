from pydantic import BaseModel,model_validator,field_validator
from typing import Literal
from Core.settings import (TYPE_KG,TYPE_GRAMM,
                           DEFAULT_MODE_VALIDATE,DEFAULT_MODE_RESPONSE,
                           DICT_MODE_VALIDATE,DICT_MODE_RESPONSE)

class Validate_Request(BaseModel):
    product : str
    mass : Literal[f'{TYPE_GRAMM}',f'{TYPE_KG}']
    number : int
    mode: Literal[f'{DEFAULT_MODE_VALIDATE}',f'{DICT_MODE_VALIDATE}'] = DEFAULT_MODE_VALIDATE
    text : str = ''

    def trasform_mode(self):
        if self.mode == DEFAULT_MODE_VALIDATE:
            self.mode = DEFAULT_MODE_RESPONSE

        elif self.mode == DICT_MODE_VALIDATE:
            self.mode = DICT_MODE_RESPONSE
            
    def transform_text(self):
        self.text = f'{self.number}{self.mass} {self.product}'
        return self