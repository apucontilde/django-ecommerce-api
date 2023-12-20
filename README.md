# DJANGO ECOMMERCE API

[Django REST framework](http://www.django-rest-framework.org/)
Based on [django-rest-framework-crud](https://github.com/juanbenitezdev/django-rest-framework-crud)

## Requirements

- Python 3.10.8
- Django 5.0
- Django REST Framework

## Installation

1. Create virtual environment

```
python -m venv .venv
```

2. Install the dependencies

```
pip install -r requirements.txt
```

## Structure

| Endpoint       | HTTP Method | CRUD Method | Result               |
| -------------- | ----------- | ----------- | -------------------- |
| `products`     | GET         | READ        | Get all products     |
| `products/:id` | GET         | READ        | Get a single product |
| `products`     | POST        | CREATE      | Create a new product |
| `products/:id` | PUT         | UPDATE      | Update a product     |
| `products/:id` | DELETE      | DELETE      | Delete a product     |

## Usage

For this example, we show how to interact with the api using httpie (`pip install httpie`)

1. Run the server, if its the first time you run it, run the migrations first.

```
python manage.py migrate
python manage.py runserver
```

2. Create super user

```
python manage.py createsuperuser
```

3. Register user

```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```

4. Get bearer token (login)

```
http http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```

```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```

- access token will be used to authenticate
- refresh token to refresh access token when expired

1. requesting new access token

```
http http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```

```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```

### Commands

```
Get all products
http http://127.0.0.1:8000/api/v1/products/ "Authorization: Bearer {YOUR_TOKEN}"
Get a single product
http GET http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}"
Create a new product
http POST http://127.0.0.1:8000/api/v1/products/ "Authorization: Bearer {YOUR_TOKEN}" title="Ant Man and The Wasp" genre="Action" year=2018
Full update a product
http PUT http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp" genre="Action" year=2018
Partial update a product
http PATCH http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp"
Delete a product
http DELETE http://127.0.0.1:8000/api/v1/products/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```

### Pagination

The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}

```
http http://127.0.0.1:8000/api/v1/products/?page=1 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/products/?page=3 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/products/?page=3&page_size=15 "Authorization: Bearer {YOUR_TOKEN}"
```

### Filters

The API supports filtering, you can filter by the attributes of a product like this

```
http http://127.0.0.1:8000/api/v1/products/?title="AntMan" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/products/?year=2020 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/products/?year__gt=2019&year__lt=2022 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/products/?genre="Action" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/products/?creator__username="myUsername" "Authorization: Bearer {YOUR_TOKEN}"
```
