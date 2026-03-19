
from Core.settings import (API_SEARCH,API_KEY,
                           INDEX_FOR_RESPONSE,
                           INDEX_FOR_GET_JSON_ERROR,
                           DEFAULT_MODE_RESPONSE,
                           DICT_MODE_RESPONSE)
import requests
from Validate.validate import ValidateApiResponse
from pydantic import ValidationError
from Core.enums import ApiJsonIndex
from Core.config_logger import get_logger

logger = get_logger(__name__)

class Nutriens():

    def __init__(self,atributs : dict):
        self.calorie = atributs.get('calorie')
        self.protein = atributs.get('protein')

class ClientSearch():

    def __init__(self, param : str, mode =DEFAULT_MODE_RESPONSE):
        self.param = param
        self.logger = logger
        self.mode = mode
    
    def get_response(self):
        self.logger.info('the method get_response in ClientSearch is started')
        self.logger.debug(f'Method get_response in ClientSearch send Api Request params:{self.param}')

        response =requests.get(API_SEARCH + f'?query={self.param}',headers={'X-Api-Key':API_KEY},)

        self.logger.info('the method get_response in ClientSearch is end')
        return response
    
    def get_json(self,response):
        self.logger.info('the method get_json in ClientSearch is started')
        status = response.status_code

        validation = ValidateApiResponse(response=response.json(),request_status=status)
        validation.dispatch()
        self.logger.info('the method get_json in ClientSearch is end')
        return validation

    def dispatch(self):
        self.logger.info('the method dispatch in ClientSearch is started')
        response = self.get_response()
        validate = self.get_json(response)

        if validate.success == True:
            self.logger.debug(f'the method dispatch in ClientSearch the validate is {validate.success}')
            json = validate.data
            status = validate.request_status
            self.logger.info('the method dispatch in ClientSearch is end')
            return self.handler(json,status)
        
        elif validate.success == False:
            self.logger.debug(f'the method dispatch in ClientSearch the validate is {validate.success} error {validate.error_message}')
            self.logger.info('the method dispatch in ClientSearch is end')
            return validate.error_message


    def handler(self,json,status):
        self.logger.info(f'the method handler in ClientSearch is started')
        if self.mode is DEFAULT_MODE_RESPONSE: 
            self.logger.debug(f'The method handler in ClientSearch return {self.mode.name}')
            self.logger.info(f'the method handler in ClientSearch is end')
            return Response(json,status)
        
        elif self.mode is DICT_MODE_RESPONSE: 
            self.logger.debug(f'The method handler in ClientSearch return {self.mode.name}')
            self.logger.info(f'the method handler in ClientSearch is end')
            return Response(json,status,mode=self.mode)
        

class Response():

    def __init__(self,json : dict, status, mode = DEFAULT_MODE_RESPONSE):
        self.json = json
        self.status = status
        self.mode = mode
        self.logger = logger
        if mode is DEFAULT_MODE_RESPONSE: 
            self.logger.debug(f'The __init__ in class Response add atribut text to eql {mode.value}')
            self.text = ''
        elif mode is DICT_MODE_RESPONSE: 
            self.logger.debug(f'The __init__ in class Response add atribut text to eql {mode.value}')
            self.text = {}
    

    def serializer(self):
        self.logger.info('The method serializer in class Response is started')
        for index in ApiJsonIndex:
            if self.mode is DEFAULT_MODE_RESPONSE: 
                self.logger.debug(f'The method serializer in class Response if mode Default add in atribut text the field : {index.name}, value: {self.json[index.value]}')
                self.text += f'{index.name}: {self.json[index.value]} \n'

            elif self.mode is DICT_MODE_RESPONSE: 
                self.logger.debug(f'The method serializer in class Response if mode Dict add in atribut text the field : {index.name}, value: {self.json[index.value]}')
                self.text[index.name] = self.json[index.value]

        self.logger.info('The method serializer in class Response is end ')
        return self.text

