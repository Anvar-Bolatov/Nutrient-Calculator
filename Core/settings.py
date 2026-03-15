from decouple import config
from .enums import Response_Mode

TYPE_KG = 'kg'
TYPE_GRAMM = 'gramm'

API_KEY = config('API_KEY')

API_SEARCH = 'https://api.calorieninjas.com/v1/nutrition'

INDEX_FOR_RESPONSE = 'items'
INDEX_FOR_GET_JSON_ERROR = 'message'
COSTANT_FOR_RETURN_ERROR_IN_VIEW = 'The params is not valid'

DEFAULT_MODE_RESPONSE = Response_Mode.TEXT
DICT_MODE_RESPONSE = Response_Mode.DICT

DEFAULT_MODE_VALIDATE = Response_Mode.TEXT.value
DICT_MODE_VALIDATE = Response_Mode.DICT.value

REQUEST_FIELDS = {'product':'Write the product for which you need to know the nutrients -> ',
                  'mass':'Write the unit of mass measurement that is convenient for you (kg, gramm) -> ',
                  'number':'Write the weight of your product -> ',
                  'mode':'Who do you need response dict or text ->',
                  'fields':['product','mass','number','mode']}

INDEX_FOR_GET_JSON_VALUE = {'calories':'calories',
                            'protein':'protein_g',
                            'fat':'fat_total_g',
                            'fields':['calories','protein','fat']}

#На будущие это еще не работает
CLASS_USE_TO_SEARCH = 'ApiClient.client.ClientSearch'
CLASS_USE_TO_CALCULAT = 'Calculator.calculator.Calculator'
CLASS_USE_TO_VALIDATE = 'Validate.validate.Form_validate'
CLASS_USE_TO_RESPONSE = 'ApiClient.client.Response'