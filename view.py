from Core.settings import REQUEST_FIELDS
from Validate.validate import Validate_Console
from pydantic import ValidationError
from ApiClient.client import ClientSearch

dict_response_inputs = {}

for i in REQUEST_FIELDS['fields']: 
    message = REQUEST_FIELDS[i]
    input_response = input(message)
    dict_response_inputs[i] = input_response

try:
    serializer = Validate_Console(**dict_response_inputs)
    serializer.transform_text()

    client = ClientSearch(serializer.text)
    print(serializer.text)

    response = client.dispatch()

    print(response.serializer())

except ValidationError :
    print(f'Данные не подходят к требованиям Валидаций') 