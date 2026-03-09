
from Core.settings import (API_SEARCH,API_KEY,INDEX_FOR_RESPONSE)
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
        
    def dispatch(self):
        response =self.get_response()
        return Response(response)
    

class Response():

    def __init__(self,response : object):
        self.response = response.json()[f'{INDEX_FOR_RESPONSE}'][0]
        self.status = response.status_code

    def serializer(self):
        if not self.status == 200:
            return f'Error:{self.response['message']} Status:{self.status}'
        
        return f"calories:{self.response['calories']}\n protein:{self.response['protein_g']}\n fat:{self.response['fat_total_g']}"



