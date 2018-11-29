# sample-rest-api-django
## About

A sample REST API developed in Python 3 using Django REST framework. It provides weight management feature with user management system.

## Project bootstrap

* Open the command line and go to the directory you want to clone the repository.  
* Clone the project: `git clone https://github.com/OrigamiStudiosLLC/sample-rest-api-django`.  
* Install pipenv: `pip install pipenv`.  
* Install the required packages: `pipenv install`.  
* Set the required environment variables from the `config/common.py` file with required values.  
* Run tests: `./manage.py test --settings=weight_management_api.config.local --configuration=Local`.  
* Run the server: `./manage.py runserver --settings=weight_management_api.config.local --configuration=Local`.  This will start the developement server at `127.0.0.1:8000`

## Endpoints

* Registers a new user:  
Request type: `POST` 
URL: `http://127.0.0.1:8000/api/v1/users/`  
Params: `username, email, password, age`  
 
 * Obtains an authentication token:  
Request type: `POST` 
URL: `http://127.0.0.1:8000/api/v1/api_token_auth/`  
Params: `username, password`  

 * Logs out an user:  
 Request type: `GET`  
 URL: `http://127.0.0.1:8000/api/v1/logout/`  
 Header: `Authorization: Token <token>`  
 
 *  Saves a new weight value:  
  Request type: `POST`  
 URL: `http://127.0.0.1:8000/api/v1/weights/`  
 Params: `weight`  
 Header `Authorization: Token <token>`  
 
 *  Lists the user's weights:   
 Request type: `GET`  
 URL: `http://127.0.0.1:8000/api/v1/weights/`  
 Header `Authorization: Token <token>`  
 
 
  

 
