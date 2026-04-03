## Project Nutrient-Calculator

## Utils 🧰

### Base : Python
### Library : Requests
### Framework : Pydantic,Pytest,Flet
### Another Utils : Docker,Postman

## **Description** 📚
The Project send request to Api CalorieNinjas( link: https://calorieninjas.com/api )

- In Project console get your params to request and send to Api or get your params using Frontend on Flet

- Wait Api  the response validating use Pydantic if Api dont response the Project send message "The Api is No a live"
- elif  is another Problem send the message the problem
  else the Project send you the Nutrient of the product

- in the Project is division in Dir Validate,ApiClient,Test,Core,Backend,Frontend for easy support the Project

  - Validate use Pydantic for validate you params in Console and Api

  - ApiClient use to send Request and Validate Api Response and get Json send use Request
 
  - Test the tests the Project use Pytest for Validate and ApiClient for incorrect case and correct 

  - Core is the configur of the Project for easy change the Fields and Params have 2 fils (settings,settings_test)

  - Backend use to create endpoint and Api using FastApi

  - Frontend used to get params and get user to send Api request( 🖼️[READ_FRONT.md]())

  - Test used for storage tests in the Project


## Warning ⚠️(if you dont use Docker Hub)
- Create logs dir in Origin Dir for Start Project or get Error
- if you want change dir name go in Dir Core and change Costant DIR_LOGGER

## How Start the Project 🔥

In origin DIR have file view.py his is the runner for Console
```
py view.py
```

In origin DIR have Dir Backend file urls.py its used for start API
```
uvicorn Backend.urls:app
```
## Docker Hub and Using Github 🏭:

Github 
```
git clone (my repository)
```
and add .env [Example](.env.example)

Create Image and start Container
```
  docker-compose up -d
```

## Using Only Docker Hub 🏭:
add .env [Example](.env.example)
```
  docker run -p 8000:8000 -v ./logs:/Nutrient-Calculator/logs --env-file .env yourbestfriend8901/nutrient-calc:latest
```
if you want start Frontend for Api use
```
  docker run -p 8500:8500 -v .\Frontend\logs:/Nutrient-Calculator_Frontend/logs yourbestfriend8901/frontend_nutrient-calc:latest
```

## How start Tests 🧪
In origin Dir have Dir tests have 3 file 
- 1 func_test utils Func for dont repeat for another 2 file in Dir Test
- 2 test_client used to test file in Dir ApiClient
- 3 test_validate used to test file in Dir Validate
Start test
```
pytest
```

## Images Tests 

![Postman Test](images/Postaman_result.PNG)
![Postman Test](images/pytest_result.PNG)
