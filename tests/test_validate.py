from Validate.validate import Validate_Request
from Core.settings_test import (CONSTANT_FOR_TEXT_REQUEST_API as TEXT_REQUEST_API,
                                CONSTANT_INCORRECT_CASE_FOR_TEXT_REQUEST_API as TEXT_BAD_REQUEST_API)
from Core.enums import RequestParams
from Core.settings import DEFAULT_MODE_RESPONSE,DICT_MODE_RESPONSE,DICT_MODE_VALIDATE
from func_test import func_test_get_validation





def test_method_trasform_mode_default_mode():
    validate_request = Validate_Request(**RequestParams.get_atributs())
    validate_request.trasform_mode()

    assert validate_request.mode == DEFAULT_MODE_RESPONSE

def test_method_trasform_mode_dict_mode():
    validate_request = Validate_Request(**RequestParams.change_mode(DICT_MODE_VALIDATE))
    validate_request.trasform_mode()

    assert validate_request.mode == DICT_MODE_RESPONSE

def test_method_trasform_text():

    obj = Validate_Request(**RequestParams.get_atributs())

    obj.transform_text()
    
    assert type(obj.text) == str
    assert obj.text == TEXT_REQUEST_API



def test_method_dispatch():
    validation = func_test_get_validation()

    validation.dispatch()

    assert validation.success == True

def test_method_dispatch_incorrect_case():
    validation = func_test_get_validation(params=TEXT_BAD_REQUEST_API)

    validation.dispatch()

    assert validation.success == False

