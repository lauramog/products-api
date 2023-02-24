# API in Django Rest Framework

This project uses Django Rest Framework (DRF) to build an API which stores two items (strings) enter by a
client 1. A  name 2. A description. In addition,  it generates automatically  A universally unique identifier  (UUID),
creation date and update date for each item.<br> for making operations as: Create, Update, delete, you can use the DRF interface as well as a terminal with the endpoints given below.<br> 
ModelSerializer class, provided for the framework  is used to process input and output data.


## :wrench: Installation 

Ensure [Docker](https://www.docker.com/get-started/) is installed locally 

You will need to create a virtual environment with python min 3.10:

```shell
python -m venv venv
```

Activate the virtual environment 

windows
```shell
venv\Scripts\activate.bat
```

mac and linux
```shell
source venv/bin/activate
```

Install the requirements
```shell
pip install -r backend/requirements.txt
```

Connect to the database

```shell
docker run -p 5432:5432 -e POSTGRES_PASSWORD=products_pass -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_USER=products_user postgres
```

Create a user; This will give you access to Django admin page, and it will create a token that you will use to interact with the Data base.

```shell
python manage.py createsuperuser
```

## Run 

Start the server
```shell
python manage.py runserver
```
Notice that development server is controlled by ASGI/Channels since we added 'channels' to INSTALLED_APPS in settings.
this configuration allow us to choose between writing synchronous code and asynchronous code, or both.<br> For now, just
Django's request/response cycle, which is synchronous cycle is implemented here. 



Access to the token generated with the command:

```shell
curl -XPOST -F 'username=your_username' -F 'password=your_password' http://localhost:port/api-token-auth/
```
If port 8000 is available, django will run the development server in it. 

You can go to the browser to use the interface provided by DRF and Django:<br>
-http://127.0.0.1:8000/  <br>
-http://127.0.0.1:8000/admin/ (you will need to enter: the user and the password that you just created in the previous steps)




### Let's populate the database using  the curl client.

| Description            | Action                |
|------------------------|-----------------------|
| post content           | POST /product/        |
| show all the content   | GET /product/         |
| Show  specific content | GET /product/uuid/    |
| update  content        | PUT /product/uuid/    |
| patch content          | PATCH /product/uuid/  |
| delete  content        | DELETE /product/uuid/ |


```shell
curl -X POST -H"Content-type:application/json" -d'{"name":"*enter_a_name*","detail":"*enter_a_description*"}' 'http://localhost:8000/product/'

```

Retrieve all the products stored in the databe

```shell
curl -X GET http://localhost:8000/product/
```
You can use the command jq to get the json data in a more readable format. Make sure you have it [installed locally](https://stedolan.github.io/jq/download/). 

```shell
curl -X GET http://localhost:8000/product/ | jq 
```
Retrieve a single product 

```shell
curl -X GET http://localhost:8000/product/*enter_product_uuid*/ | jq 
```

Delete a single product 

```shell
curl -X DELETE http://localhost:8000/product/*enter_product_uuid*/
```

Update a single product 

```shell
curl -X PUT -H"Content-type:application/json" -d'{"name":"*enter_a_name*","detail":"*enter_a_description*"}' 'http://localhost:8000/product/*enter_product_uuid*/'

```

Update a specific field for a single product 

```shell
curl -X PATCH -H"Content-type:application/json" -d'{"name":"*enter_a_name*","detail":"*enter_a_description*"}' 'http://localhost:8000/product/*enter_product_uuid*/'

```











