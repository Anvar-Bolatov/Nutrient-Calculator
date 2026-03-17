
from Core.settings import (API_SEARCH,API_KEY,
                           INDEX_FOR_RESPONSE,
                           INDEX_FOR_GET_JSON_VALUE,
                           INDEX_FOR_GET_JSON_ERROR,
                           DEFAULT_MODE_RESPONSE,
                           DICT_MODE_RESPONSE)
import requests

from Core.config_logger import get_logger

logger = get_logger(__name__)

class Nutriens():

    def __init__(self,atributs : dict):
        self.calorie = atributs.get('calorie')
        self.protein = atributs.get('protein')

class ClientSearch(): # Need Refacting this part the code ALL because lot of if and hard to read and support 

    def __init__(self, param : str):
        self.param = param
        self.logger = logger
    
    def get_response(self):
        self.logger.info(f'Method get_response in ClientSearch send Api Request params:{self.param}')
        return requests.get(API_SEARCH + f'?query={self.param}',headers={'X-Api-Key':API_KEY},)

    def get_json(self,response): # Refactoring need Validate in Pydantic for more support code and reading 
        status = response.status_code

        if not status == requests.codes.ok:
            try:
                error_message = response.json()[INDEX_FOR_GET_JSON_ERROR]
                self.logger.info(f'The method get_json in ClientSearch if status not {requests.codes.ok} check if Json have message return Message: {error_message}, status:{status}')
                return error_message,status
            
            except ValueError:
                self.logger.error(f'The method get_json in ClientSearch if status not {requests.codes.ok} and Null return Message:None, status:{status} ')
                return None,status
        try:
            response_value = response.json()[INDEX_FOR_RESPONSE][0]
            status = response.status_code
            self.logger.info(f'The Json is not Null and have status {status}')
            return response_value,status
        
        except IndexError:
            self.logger.error(f'The Json have status:{status} it null')
            return None,status
    
    def dispatch(self,mode=DEFAULT_MODE_RESPONSE):
        response =self.get_response()
        json,status = self.get_json(response)

        if not status == requests.codes.ok:  # Refactoring hard to reading the code and support
            if json:
                self.logger.error(f'The method Dispatch in ClientSearch if status not {requests.codes.ok} and have Json return Message:{json}, status:{status}')
                return f'Message:{json} Status:{status}'
            else:
                self.logger.error(f'The method Dispatch in ClientSearch if status not {requests.codes.ok} and dont have Json return Message:Null, status:{status}')
                return f'Response Api is null Status:{status}'
        
        elif not json:
            self.logger.info(f'The method Dispatch in ClientSearch if status {requests.codes.ok} and dont have Json return Message:Null, status{status}')
            return f'Response Api is null Status:{status}'
    
        if mode is DEFAULT_MODE_RESPONSE: 
            self.logger.info(f'The method Dispatch in ClientSearch if mode is Default return text')
            return Response(json,status)
        
        elif mode is DICT_MODE_RESPONSE: 
            self.logger.info(f'The method Dispatch in ClientSearch if mode is Default return json')
            return Response(json,status,mode=DICT_MODE_RESPONSE)

class Response():

    def __init__(self,json : dict, status, mode = DEFAULT_MODE_RESPONSE):
        self.json = json
        self.status = status
        self.mode = mode
        self.logger = logger
        if mode is DEFAULT_MODE_RESPONSE: 
            self.logger.debug('The __init__ in class Response add atribut text to eql str')
            self.text = ''
        elif mode is DICT_MODE_RESPONSE: 
            self.logger.debug('The __init__ in class Response add atribut text to eql dict')
            self.text = {}

    def serializer(self):
        self.logger.info('The method serializer in class Response is started')
        for i in INDEX_FOR_GET_JSON_VALUE['fields']:
                field_value = INDEX_FOR_GET_JSON_VALUE[i]

                if self.mode is DEFAULT_MODE_RESPONSE: 
                    self.logger.debug(f'The method serializer in class Response if mode Default add in atribut text the field : {i}, value: {self.json[field_value]}')
                    self.text += f'{i}: {self.json[field_value]} \n'

                elif self.mode is DICT_MODE_RESPONSE: 
                    self.logger.debug(f'The method serializer in class Response if mode Dict add in atribut text the field : {i}, value: {self.json[field_value]}')
                    self.text[i] = self.json[field_value]

        self.logger.info('The method serializer in class Response is end ')
        return self.text


