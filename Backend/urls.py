from fastapi import FastAPI,Response,status
from Validate.validate import Validate_Request
from ApiClient.client import ClientSearch
from Core.settings import DICT_MODE_RESPONSE



app = FastAPI()

@app.get('/product/')
async def watch_product_view():
    return {'status':'ok'}

@app.post('/product/')
async def validate_product_view(product:Validate_Request, response: Response):
    product.transform_text()
    text = product.text
    print(text)
    clientsearch = ClientSearch(text)

    response_dispatch = clientsearch.dispatch(mode=DICT_MODE_RESPONSE)

    if isinstance(response_dispatch,str):
        response.status_code = status.HTTP_400_BAD_REQUEST    
        return{'message': response_dispatch}
        
    else:
        response.status_code = status.HTTP_200_OK
        response_dispatch.serializer()
        return{'items':response_dispatch.text}
 