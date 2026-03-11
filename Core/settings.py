from decouple import config

TYPE_KG = 'kg'
TYPE_GRAMM = 'gramm'

API_KEY = config('API_KEY')

API_SEARCH = 'https://api.calorieninjas.com/v1/nutrition'

INDEX_FOR_RESPONSE = 'items'

REQUEST_FIELDS = {'product':'Write the product for which you need to know the nutrients -> ',
                  'mass':'Write the unit of mass measurement that is convenient for you (kg, gramm) -> ',
                  'number':'Write the weight of your product -> ',
                  'fields':['product','mass','number']}

INDEX_FOR_GET_JSON_VALUE = {'calories':'calories',
                            'protein':'protein_g',
                            'fat':'fat_total_g',
                            'fields':['calories','protein','fat']}

#На будущие это еще не работает
CLASS_USE_TO_SEARCH = 'ApiClient.client.ClientSearch'
CLASS_USE_TO_CALCULAT = 'Calculator.calculator.Calculator'
CLASS_USE_TO_VALIDATE = 'Validate.validate.Form_validate'
CLASS_USE_TO_RESPONSE = 'ApiClient.client.Response'