from Validate.validate import Validate_Console
from Core.settings_test import (CONSTANT_FOR_TEXT_REQUEST_API,
                                CONSTANT_FOR_PARAMS)

def test_validate_trasform_dict():
    result = Validate_Console.trasform_dict(**CONSTANT_FOR_PARAMS)
    assert type(result) == dict

    product = result['product']
    assert type(product) == str
    assert product == 'Meat'

    mass = result['mass']
    assert type(mass) == str
    assert mass == 'kg'

    number = result['number']
    assert type(number) == str
    assert number == '10'

def test_trasform_text_return():
    dict_for_serializer = Validate_Console.trasform_dict("Meat",'kg','10')
    obj = Validate_Console(**dict_for_serializer)

    obj.transform_text()
    
    assert type(obj.text) == str
    assert obj.text == CONSTANT_FOR_TEXT_REQUEST_API
