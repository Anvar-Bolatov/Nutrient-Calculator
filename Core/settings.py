from decouple import config
from .enums import Response_Mode
from enum import Enum

TYPE_KG = 'kg'
TYPE_GRAMM = 'gramm'

API_KEY = config('API_KEY')

API_SEARCH = 'https://api.calorieninjas.com/v1/nutrition'

DIR_LOGGER = 'logs'
MAX_MB_ROTATING_LOGS = 10 

INDEX_FOR_RESPONSE = 'items'
INDEX_FOR_GET_JSON_ERROR = 'message'
COSTANT_FOR_RETURN_ERROR_IN_VIEW = 'The params is not valid'

DEFAULT_MODE_RESPONSE = Response_Mode.TEXT
DICT_MODE_RESPONSE = Response_Mode.DICT

DEFAULT_MODE_VALIDATE = Response_Mode.TEXT.value
DICT_MODE_VALIDATE = Response_Mode.DICT.value


#На будущие это еще не работает
CLASS_USE_TO_SEARCH = 'ApiClient.client.ClientSearch'
CLASS_USE_TO_CALCULAT = 'Calculator.calculator.Calculator'
CLASS_USE_TO_VALIDATE = 'Validate.validate.Form_validate'
CLASS_USE_TO_RESPONSE = 'ApiClient.client.Response'