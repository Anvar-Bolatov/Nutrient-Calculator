from fastapi import FastAPI,Response,status
from Validate.validate import Validate_Request
from ApiClient.client import ClientSearch
from Core.settings import DICT_MODE_RESPONSE
from Core.config_logger import get_logger
from requests import codes

logger = get_logger(__name__)

app = FastAPI()

@app.get('/product/')
async def watch_product_view():
    logger.info(f'The view Heal is actived and return status {codes.ok}')
    return {'status':'ok'}

@app.post('/product/')
async def validate_product_view(product:Validate_Request, response: Response):
    logger.info('The view "validate_product_view" in urls is anctived')
    product.transform_text()
    text = product.text
    
    logger.debug(f'Trasform the Json body in text:{text} for Request Api ')
    logger.debug('"validate_product_view" send request the Api')
    clientsearch = ClientSearch(text)

    response_dispatch = clientsearch.dispatch(mode=DICT_MODE_RESPONSE) # Refactoring
    logger.debug('Get the object Response or the text error')

    if isinstance(response_dispatch,str):
        logger.error(f'"validate_product_view" send error text : {response_dispatch} ')
        response.status_code = status.HTTP_400_BAD_REQUEST    
        return{'message': response_dispatch}
        
    else:
        logger.info('"validate_product" send the Nutrient')
        response.status_code = status.HTTP_200_OK
        logger.debug('Trasform the Json or text for send Nutrient')
        response_dispatch.serializer()
        return{'items':response_dispatch.text}
 