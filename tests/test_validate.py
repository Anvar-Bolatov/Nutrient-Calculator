from Validate.validate import Validate_Console
from Core.settings_test import (CONSTANT_FOR_TEXT_REQUEST_API,
                                CONSTANT_FOR_PARAMS)


def test_trasform_text_return():
    
    obj = Validate_Console(**CONSTANT_FOR_PARAMS)

    obj.transform_text()
    
    assert type(obj.text) == str
    assert obj.text == CONSTANT_FOR_TEXT_REQUEST_API
