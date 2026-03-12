from ApiClient.client import ClientSearch
from requests.models import Response
from Core.settings_test import (CONSTANT_FOR_TEXT_REQUEST_API,
                                RESPONSE_FIELDS_TO_TEST,
                                CONSTANT_INCORRECT_CASE_FOR_TEXT_REQUEST_API as INCORRECT_CASE_FOR_TEXT)
from requests import codes
def test_class_response_return():
    client_obj  = ClientSearch(CONSTANT_FOR_TEXT_REQUEST_API)
    response_obj = client_obj.dispatch()

    list_field_value = []

    for i in RESPONSE_FIELDS_TO_TEST['fields']:
        field_index = RESPONSE_FIELDS_TO_TEST[i]
        field_value = response_obj.json[field_index]
        assert type(field_value) == float
        list_field_value.append(field_value)


    response_obj.serializer()

    assert type(response_obj.text) == str
    for i in list_field_value:
        assert str(i) in response_obj.text

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


