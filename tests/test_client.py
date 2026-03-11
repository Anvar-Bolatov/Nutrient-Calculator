from ApiClient.client import ClientSearch
from Core.settings_test import CONSTANT_FOR_TEXT_REQUEST_API,RESPONSE_FIELD_TO_TEST

def test_class_response_return():
    client_obj  = ClientSearch(CONSTANT_FOR_TEXT_REQUEST_API)
    response_obj = client_obj.dispatch()

    list_field_value = []

    for i in RESPONSE_FIELD_TO_TEST['fields']:
        field_index = RESPONSE_FIELD_TO_TEST[i]
        field_value = response_obj.json[field_index]
        assert type(field_value) == float
        list_field_value.append(field_value)


    response_obj.serializer()

    assert type(response_obj.text) == str
    for i in list_field_value:
        assert str(i) in response_obj.text
