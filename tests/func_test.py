from ApiClient.client import ClientSearch
from Core.settings_test import CONSTANT_FOR_TEXT_REQUEST_API as TEXT_REQUEST_API
from Core.settings import DICT_MODE_RESPONSE,DEFAULT_MODE_RESPONSE
from Validate.validate import ValidateApiResponse

def func_test_get_response(params=TEXT_REQUEST_API,mode=DEFAULT_MODE_RESPONSE):
    client_search = ClientSearch(params,mode)

    response = client_search.get_response()

    return response,client_search

def func_test_get_json(params=TEXT_REQUEST_API,mode=DEFAULT_MODE_RESPONSE):
    response,obj =func_test_get_response(params,mode)
    json = obj.get_json(response)
    return json,obj

def func_test_get_validation(params=TEXT_REQUEST_API):
    response,client_search =func_test_get_response(params)
    status = response.status_code

    validation = ValidateApiResponse(response=response.json(),request_status=status)
    return validation

def func_test_get_response_serializer(mode=DEFAULT_MODE_RESPONSE):
    client_search = ClientSearch(TEXT_REQUEST_API,mode=mode)
    response = client_search.dispatch()

    return response