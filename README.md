#API in Django Rest Framework

This project uses Django Rest Framework (DRF) to build an API which stores two items (strings) enter by a client 1. A  name 2. A description. In addition  it generates automaticly  A universally unique identifier  (UUID), creation date and update date for each item. 

## :wrench: Installation 
You will need to create a virtual enviroment with python =>3.10.

```shell
python -m venv venv
```

Activate the virtual enviroment 

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

Create a user. This will give you access to Django admin page, an it will create a token that you will use to interact with the Data base.

```shell
python manage.py createsuperuser
```

## Run 

Start the server
```shell
python manage.py runserver
```

Access to the token generated with the command:

```shell
curl -XPOST -F 'username=yourusername' -F 'password=yourpassword' http://localhost:port/api-token-auth/
```
If port 8000 is available, django will run the development server in it. 

You can go to the browser to use the interface provided by DRF and Django:
*http://127.0.0.1:8000/
*http://127.0.0.1:8000/admin/ (you will need to enter: the user and the password that you just created in the previous steps)

### Let's use the curl client for CRUD operations.

Populate the DB from your terminal making a POST request: 

```shell
curl -H"Content-type:application/json" -d'{"name":"*enteraname*","detail":"*enteradescription*"}' 'http://localhost:8000/product/'

```

Retrieve all the items store in the DB.

```shell
curl http://localhost:8000/productlisting/
```














