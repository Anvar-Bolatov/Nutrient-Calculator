
product = input('Write the product for which you need to know the nutrients -> ')
mass = input('Write the unit of mass measurement that is convenient for you (kg, gramm) -> ')
number = input('Write the weight of your product -> ')


from Validate.validate import Validate_Console
from pydantic import ValidationError

dict_for_serializer = Validate_Console.trasform_dict(product,mass,number)

try:
    serializer = Validate_Console(**dict_for_serializer)
    serializer.transform_text()

    from ApiClient.client import ClientSearch

    client = ClientSearch(serializer.text)
    print(serializer.text)

    response = client.dispatch()

    print(response.serializer())

except ValidationError :
    print(f'Данные не подходят к требованиям Валидаций') 