from Core.settings import (REQUEST_FIELDS,
                           COSTANT_FOR_RETURN_ERROR_IN_VIEW)
from Validate.validate import Validate_Request
from pydantic import ValidationError
from ApiClient.client import ClientSearch

dict_response_inputs = {}

for i in REQUEST_FIELDS['fields']: 
    message = REQUEST_FIELDS[i]
    input_response = input(message)
    dict_response_inputs[i] = input_response

try:
    serializer = Validate_Request(**dict_response_inputs)
    serializer.transform_text()
    serializer.trasform_mode()

    client = ClientSearch(serializer.text)
    print(serializer.text)


    response = client.dispatch(mode=serializer.mode)

    if type(response) is str:
        print(response)

    else:
        response.serializer()
        print(response.text)

except ValidationError :
    print(COSTANT_FOR_RETURN_ERROR_IN_VIEW) 