# DJANGO ECOMMERCE API

[Django REST framework](http://www.django-rest-framework.org/)
Based on [django-rest-framework-crud](https://github.com/juanbenitezdev/django-rest-framework-crud) & [django-github-digitalocean](https://github.com/testdrivenio/django-github-digitalocean)

## Requirements

- Python 3.10.8
- Django 5.0
- Django REST Framework
- Docker

## Installation

1. Create virtual environment

```bash
python -m venv .venv
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

## Structure

| Endpoint      | HTTP Method | CRUD Method | Result               |
| ------------- | ----------- | ----------- | -------------------- |
| `product`     | GET         | READ        | Get all product      |
| `product/:id` | GET         | READ        | Get a single product |
| `product`     | POST        | CREATE      | Create a new product |
| `product/:id` | PUT         | UPDATE      | Update a product     |
| `product/:id` | DELETE      | DELETE      | Delete a product     |
TODO: order, cart structures?

## Usage

For this example, we show how to interact with the api using httpie (`pip install httpie`)

1. Run the server, if its the first time you run it, run the migrations first.

```bash
python manage.py migrate
python manage.py runserver
```

2. Create super user

```bash
python manage.py createsuperuser
```

3. Register user

```bash
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```

4. Get bearer token (login)

```bash
http http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```

- access token will be used to authenticate
- refresh token to refresh access token when expired

1. requesting new access token

```bash
http http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```

### Commands

```bash
# Get all product
http http://127.0.0.1:8000/api/v1/product/ "Authorization: Bearer {YOUR_TOKEN}"
# Get a single product
http GET http://127.0.0.1:8000/api/v1/product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}"
# Create a new product
http POST http://127.0.0.1:8000/api/v1/product/ "Authorization: Bearer {YOUR_TOKEN}" title="Ant Man and The Wasp" genre="Action" year=2018
# Full update a product
http PUT http://127.0.0.1:8000/api/v1/product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp" genre="Action" year=2018
# Partial update a product
http PATCH http://127.0.0.1:8000/api/v1/product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="AntMan and The Wasp"
# Delete a product
http DELETE http://127.0.0.1:8000/api/v1/product/{product_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```

### Pagination

The API supports pagination, by default responses have a page_size=10 but if you want change that you can pass through params page_size={your_page_size_number}

```bash
http http://127.0.0.1:8000/api/v1/product/?page=1 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/product/?page=3 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/product/?page=3&page_size=15 "Authorization: Bearer {YOUR_TOKEN}"
```

### Filters

The API supports filtering, you can filter by the attributes of a product like this

```bash
http http://127.0.0.1:8000/api/v1/product/?short_name="Cup" "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/product/?price_gt=10 "Authorization: Bearer {YOUR_TOKEN}"
http http://127.0.0.1:8000/api/v1/product/?category="Clothing" "Authorization: Bearer {YOUR_TOKEN}"
```
