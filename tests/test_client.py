from ApiClient.client import ClientSearch,Response
from requests.models import Response as request_Response
from Core.settings_test import (CONSTANT_FOR_TEXT_REQUEST_API as TEXT_REQUEST_API,
                                CONSTANT_INCORRECT_CASE_FOR_TEXT_REQUEST_API as BAD_REQUEST)

from Core.settings import (DEFAULT_MODE_RESPONSE,
                           DICT_MODE_RESPONSE)

from Validate.validate import ValidateApiResponse
from tests.func_test import (func_test_get_json,func_test_get_response,
                             func_test_get_response_serializer)
from ApiClient.client import ClientSearch
from requests import codes
from Core.enums import ApiJsonIndex

def test_method_get_response():
    response,obj = func_test_get_response()

    assert isinstance(response,request_Response)


def test_method_get_json():
    
    validation,obj = func_test_get_json(TEXT_REQUEST_API)

    assert isinstance(validation,ValidateApiResponse)


def test_method_get_json_incorrect_case():
    validation,obj = func_test_get_json(BAD_REQUEST)

    assert validation.success == False
    assert isinstance(validation,ValidateApiResponse)

def test_method_dispatch():
    client_search = ClientSearch(TEXT_REQUEST_API)
    response = client_search.dispatch()

    assert response.mode == DEFAULT_MODE_RESPONSE

def test_method_dispatch_incorrect_case():
    validate,obj = func_test_get_json(BAD_REQUEST)
    response = obj.dispatch()

    assert validate.success == False
    assert validate.error_message == response

def test_method_handler_mode_text():
    validate,obj = func_test_get_json(TEXT_REQUEST_API)

    response = obj.handler(validate.data,validate.request_status)
    mode = response.mode

    assert mode == DEFAULT_MODE_RESPONSE
    assert isinstance(response,Response)

def test_method_handler_mode_dict():
    validate,obj = func_test_get_json(TEXT_REQUEST_API,mode=DICT_MODE_RESPONSE)

    response = obj.handler(validate.data,validate.request_status)
    mode = response.mode

    assert mode == DICT_MODE_RESPONSE
    assert isinstance(response,Response)



def test_class_Respose_text():
    response = func_test_get_response_serializer()

    assert isinstance(response.text,str)


def test_class_Respose_dict():
    response = func_test_get_response_serializer(mode=DICT_MODE_RESPONSE)

    assert isinstance(response.text,dict)


def test_method_serializer_text():
    response = func_test_get_response_serializer()
    keys = ApiJsonIndex.get_keys()
    response.serializer()

    for key in keys:
        assert key in response.text


def test_method_serializer_dict():
    response = func_test_get_response_serializer(mode=DICT_MODE_RESPONSE)
    keys = ApiJsonIndex.get_keys()
    response.serializer()

    for key in keys:
        assert key in response.text
