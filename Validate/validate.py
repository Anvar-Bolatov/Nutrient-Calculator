from pydantic import BaseModel,model_validator,field_validator
from typing import Literal
from Core.settings import (TYPE_KG,TYPE_GRAMM,
                           DEFAULT_MODE_VALIDATE,DEFAULT_MODE_RESPONSE,
                           DICT_MODE_VALIDATE,DICT_MODE_RESPONSE)

from Core.config_logger import get_logger

logger = get_logger(__name__)

class Validate_Request(BaseModel):
    product : str
    mass : Literal[f'{TYPE_GRAMM}',f'{TYPE_KG}']
    number : int
    mode: Literal[f'{DEFAULT_MODE_VALIDATE}',f'{DICT_MODE_VALIDATE}'] = DEFAULT_MODE_VALIDATE
    text : str = ''

    def trasform_mode(self):
        logger.debug('The method trasform_mode in Validate_Request started')
        if self.mode == DEFAULT_MODE_VALIDATE:
            logger.debug(f'The method trasform_mode in Validate_Request transform mode: {self.mode} in {DEFAULT_MODE_RESPONSE}')
            self.mode = DEFAULT_MODE_RESPONSE

        elif self.mode == DICT_MODE_VALIDATE:
            logger.debug(f'The method trasform_mode in Validate_Request transform mode: {self.mode} in {DICT_MODE_RESPONSE}')
            self.mode = DICT_MODE_RESPONSE
            
    def transform_text(self):
        self.text = f'{self.number}{self.mass} {self.product}'
        logger.debug(f'The method trasform_text in class Validate_Request text:{self.text}')
        return self