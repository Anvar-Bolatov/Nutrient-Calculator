from enum import Enum

class Response_Mode(Enum):
    TEXT = 'text'
    DICT = 'dict'

class RequestFieldsMessage(Enum):
    product = 'Write the product for which you need to know the nutrients -> '
    mass = 'Write the unit of mass measurement that is convenient for you (kg, gramm) -> '
    number ='Write the weight of your product -> '
    mode = 'Who do you need response dict or text ->'

class RequestParams(Enum):
    product = 'Meat'
    mass = 'kg'
    number = '10'
    mode = 'text'

    @staticmethod
    def get_atributs():
        params = {}
        for param in RequestParams:
            params[param.name] = param.value
        return params
    
    @staticmethod
    def change_mode(mode):
        atributs =RequestParams.get_atributs()
        atributs['mode'] = mode
        return atributs


class ApiJsonIndex(Enum):
    calories = 'calories'
    protein = 'protein_g'
    fat = 'fat_total_g'

    @staticmethod
    def get_keys():
        keys = []
        for key in ApiJsonIndex:
            keys.append(key.name)
        return keys