from Core.settings import (COSTANT_FOR_RETURN_ERROR_IN_VIEW)
from Core.enums import RequestFieldsMessage
from Validate.validate import Validate_Request
from pydantic import ValidationError
from ApiClient.client import ClientSearch


dict_response_inputs = {}


for i in RequestFieldsMessage:
    input_response = input(i.value)
    dict_response_inputs[i.name] = input_response

try:
    serializer = Validate_Request(**dict_response_inputs)
    serializer.transform_text()
    serializer.trasform_mode()

    client = ClientSearch(serializer.text,mode=serializer.mode)
    print(serializer.text)


    response = client.dispatch()


    if type(response) is str:
        print(response)

    else:
        response.serializer()
        print(response.text)

except ValidationError :
    print(COSTANT_FOR_RETURN_ERROR_IN_VIEW) 