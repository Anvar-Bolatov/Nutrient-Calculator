## Project Nutrient-Calculator

## Utils
Python,Pydantic,Pytest,Request

## **Description** 
The Project send request to Api CalorieNinjas( link: https://calorieninjas.com/api )

- In Project console get your params to request and send to Api

- Wait the Api response and validate the response if params is not good the Api send Null and the Project write "The response is null"
  else the Project send you the Nutrient of the product

- in the Project is division in Dir Validate,ApiClient,Test,Core for easy support the Project

  - Validate use Pydantic for validate you params in Console

  - ApiClient use to send Request and Validate Api Response and get Json send use Request
 
  - Test the tests the Project use Pytest for Validate and ApiClient for incorrect case and correct 

  - Core is the configur of the Project for easy change the Fields and Params have 2 fils (settings,settings_test)

## How Start the Project

In origin DIR have file view.py his is the runner
```
py view.py
```
