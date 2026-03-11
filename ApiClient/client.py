
from Core.settings import (API_SEARCH,API_KEY,
                           INDEX_FOR_RESPONSE,INDEX_FOR_GET_JSON_VALUE)
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

    def get_json(self,response):
        try:
            response_value = response.json()[INDEX_FOR_RESPONSE][0]

        except KeyError:
            return None,response.status_code
        
        return response_value,response.status_code
    
    def dispatch(self):
        response =self.get_response()
        json,status = self.get_json(response)

        if json and status == 200:
            return Response(json,status)
        
        elif json['message']:
            return f'Message:{json['message']}'
                     
        else: 
            return f"Response Api is null \n Status: {status}" 

class Response():

    def __init__(self,json : dict, status):
        self.json = json
        self.status = status
        self.text = ''

    def serializer(self):

        for i in INDEX_FOR_GET_JSON_VALUE['fields']:
            field_value = INDEX_FOR_GET_JSON_VALUE[i]
            self.text += f'{i}: {self.json[field_value]} \n'

        return self.text


