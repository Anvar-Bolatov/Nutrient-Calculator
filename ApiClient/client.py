
from Core.settings import (API_SEARCH,API_KEY,
                           INDEX_FOR_RESPONSE,
                           INDEX_FOR_GET_JSON_VALUE,
                           INDEX_FOR_GET_JSON_ERROR,
                           DEFAULT_MODE_RESPONSE,
                           DICT_MODE_RESPONSE)
import requests

class Nutriens():

    def __init__(self,atributs : dict):
        self.calorie = atributs.get('calorie')
        self.protein = atributs.get('protein')



class ClientSearch():

    def __init__(self, param : str):
        self.param = param
    
    def get_response(self):
        return requests.get(API_SEARCH + f'?query={self.param}',headers={'X-Api-Key':API_KEY},)

    def get_json(self,response): # Refactoring need Validate in Pydantic for more support code and reading 
        status = response.status_code

        if not status == requests.codes.ok:
            try:
                return response.json()[INDEX_FOR_GET_JSON_ERROR],status
            
            except ValueError:
                return None,status
        try:
            response_value = response.json()[INDEX_FOR_RESPONSE][0]
            status = response.status_code
            return response_value,status
        except IndexError:
            return None,status
    
    def dispatch(self,mode=DEFAULT_MODE_RESPONSE):
        response =self.get_response()
        json,status = self.get_json(response)

        if not status == requests.codes.ok:  # Refactoring hard to reading the code and support
            if json:
                return f'Message:{json} \n Status:{status}'
            else:
                return f'Response Api is null \n Status:{status}'
        
        elif not json:
            return f'Response Api is null \n Status:{status}'
        
        if mode is DEFAULT_MODE_RESPONSE: 
            return Response(json,status)
        
        elif mode is DICT_MODE_RESPONSE: 
            return Response(json,status,mode=DICT_MODE_RESPONSE)

class Response():

    def __init__(self,json : dict, status, mode = DEFAULT_MODE_RESPONSE):
        self.json = json
        self.status = status
        self.mode = mode

        if mode is DEFAULT_MODE_RESPONSE: 
            self.text = ''
        elif mode is DICT_MODE_RESPONSE: 
            self.text = {}

    def serializer(self):
        for i in INDEX_FOR_GET_JSON_VALUE['fields']:
                field_value = INDEX_FOR_GET_JSON_VALUE[i]

                if self.mode is DEFAULT_MODE_RESPONSE: 
                    self.text += f'{i}: {self.json[field_value]} \n'

                elif self.mode is DICT_MODE_RESPONSE: 
                    self.text[i] = self.json[field_value]

        return self.text


