from decouple import config

TYPE_KG = 'kg'
TYPE_GRAMM = 'gramm'

API_KEY = config('API_KEY')

API_SEARCH = 'https://api.calorieninjas.com/v1/nutrition'

INDEX_FOR_RESPONSE = 'items'

#На будущие это еще не работает
CLASS_USE_TO_SEARCH = 'ApiClient.client.ClientSearch'
CLASS_USE_TO_CALCULAT = 'Calculator.calculator.Calculator'
CLASS_USE_TO_VALIDATE = 'Validate.validate.Form_validate'
CLASS_USE_TO_RESPONSE = 'ApiClient.client.Response'