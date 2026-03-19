from pydantic import BaseModel,model_validator,field_validator,ValidationError
from typing import Literal,Optional
from requests import Response
from Core.settings import (TYPE_KG,TYPE_GRAMM,
                           DEFAULT_MODE_VALIDATE,DEFAULT_MODE_RESPONSE,
                           DICT_MODE_VALIDATE,DICT_MODE_RESPONSE,
                           INDEX_FOR_GET_JSON_ERROR,INDEX_FOR_RESPONSE)

from requests import codes
from Core.config_logger import get_logger

logger = get_logger(__name__)

class Validate_Request(BaseModel):
    product : str
    mass : Literal[f'{TYPE_GRAMM}',f'{TYPE_KG}']
    number : int
    mode: Literal[f'{DEFAULT_MODE_VALIDATE}',f'{DICT_MODE_VALIDATE}'] = DEFAULT_MODE_VALIDATE
    text : Optional[str] = ''

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
    
class ValidateApiResponse(BaseModel):
    response : dict
    request_status : int
    success : Optional[bool] = None
    data : Optional[dict] = None
    error_message: Optional[str] = None

    def response_error(self,error):
        self.success = False
        self.error_message = error

    
    def dispatch(self):
        if self.request_status != codes.ok:
            self.incorrect_status()

        else:
            self.correct_status()


    def incorrect_status(self):
        try:
            logger.info('the method incorrect_status started')
            error_message = self.response[INDEX_FOR_GET_JSON_ERROR]
            self.success = False
            logger.info('the method incorrect_status end')

        except ValueError:
            logger.error(f'The method get_json in ClientSearch if status not {codes.ok} and Null return Message:None, status:{self.request_status} ')
            self.response_error(f'Api is not a Live {self.request_status}') 
        

    def correct_status(self):
        try:
            logger.info('the method correct_status started')
            response_value = self.response[INDEX_FOR_RESPONSE][0]
            logger.debug(f'The Json is not Null and have status {self.request_status}')
            self.data = response_value
            self.success = True
            logger.info('the method correct_status end')
        
        except IndexError:
            logger.error(f'The Json have status:{self.request_status} it null')
            self.response_error(f'Bad Request The Api Response is null status:{self.request_status}')
    