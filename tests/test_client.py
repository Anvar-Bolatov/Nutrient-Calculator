from ApiClient.client import ClientSearch
from requests.models import Response
from Core.settings_test import (CONSTANT_FOR_TEXT_REQUEST_API,
                                RESPONSE_FIELDS_TO_TEST,
                                CONSTANT_INCORRECT_CASE_FOR_TEXT_REQUEST_API as INCORRECT_CASE_FOR_TEXT)

from Core.settings import (DEFAULT_MODE_RESPONSE,
                           DICT_MODE_RESPONSE,
                           INDEX_FOR_GET_JSON_VALUE as JSON_KEY)

from requests import codes

def test_class_response_return_text(): # the test is big this not good to support the code
    client_search_obj  = ClientSearch(CONSTANT_FOR_TEXT_REQUEST_API)
    response_text_obj = client_search_obj.dispatch()
    response_dict_obj = client_search_obj.dispatch(mode=DICT_MODE_RESPONSE)

    list_field_value_text = []
    list_field_value_dict = []

    for i in RESPONSE_FIELDS_TO_TEST['fields']:
        field_index = RESPONSE_FIELDS_TO_TEST[i]
        field_value_text = response_text_obj.json[field_index]
        field_value_dict = response_dict_obj.json[field_index]

        assert isinstance(field_value_text,float)
        assert isinstance(field_value_dict,float) 

        list_field_value_text.append(field_value_text)
        list_field_value_dict.append(field_value_dict)

    response_text_obj.serializer()
    response_dict_obj.serializer()

    assert response_text_obj.mode is DEFAULT_MODE_RESPONSE
    assert response_dict_obj.mode is DICT_MODE_RESPONSE

    for i in list_field_value_text:
        assert str(i) in response_text_obj.text
    
    for i in JSON_KEY['fields']:
        key_value = JSON_KEY[i]
        json_response = response_dict_obj.text
        json_value = response_dict_obj.json[key_value]

        assert json_response[i] == json_value
        assert isinstance(json_response[i],float)

def test_incorrect_case_class_ClientSearch_method():
    client_obj = ClientSearch(INCORRECT_CASE_FOR_TEXT)

    response = client_obj.get_response()
    assert isinstance(response,Response)

    json,status = client_obj.get_json(response)
    assert status == codes.ok
    assert json == None

def test_incorrect_case_class_ClientSearch_method_dispatch():
    client_obj = ClientSearch(INCORRECT_CASE_FOR_TEXT)
    response = client_obj.dispatch()

    assert str(codes.ok) in response


