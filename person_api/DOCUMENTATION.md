# Simple Person API Documentation

## Introduction

Welcome to the official documentation for https://hngx.kasyoki.africa/api/. This API is built on Django and uses an SQLite database. This document provides an overview of the key features, installation instructions, usage guidelines, and other important information about the app.

## Table of Contents

- [Installation](#installation)
- [UML Design Diagrams](#uml-design-diagrams)
- [API Endpoints and Examples](#api-endpoints)
- [Testing](#testing)
- [Limitations](#limitations)

## Installation

1. Clone the repo
2. Change directory to the person_api directory. For linux `cd hngx2`
3. Install pip into your environment
4. Install pipenv using pip `pip install pipenv`
5. Create a virtual env with `pipenv shell`
6. Install requirements `pipenv install`
7. Create database tables `python manage.py migrate`
8. Run the API `python manage.py runserver`
9. Access the api at `http://localhost:8000/api/`

## UML Design Diagrams

### Person ERD

![Person Entity Diagram](../UML_Designs/person_entity.png)

### API Design

![API Design](../UML_Designs/person_api.drawio.png)

## API Endpoints and Examples

Sections show the URL, and method type accepted

### `/api/` [GET]

- Lists all person resources stored in the database. The response contains a set of objects for all person resources stored.

- Response (Success):

  ```
  [{ "id":1, "name":"Person Name" }]
  ```

### `/api/` [POST]

- Creates a new person if called with POST. Accepts JSON:
  ```
  { "name" : "Person Name" }
  ```
- Response (Success : 201):
  ```
  [{ "id":1, "name":"Person Name" }]
  ```

### `/api/<str:name>/` [GET, PUT, DELETE]

#### GET

- For the GET, returns the id and name of the resource in the format

  - Response (Success : 200):
    ```
    {"id": 1, "name": "Person Name" }
    ```

#### PUT

- For PUT, it allows the manipulation of a particular person resource stored in the API.

  Accepts JSON:

  ```
  { "name": "New Person Name" }
  ```

- PUT Response (Success : 200):
  ```
  {"id": 1, "name": "Person Name" }
  ```

#### DELETE

- For DELETE, it allows the removal of a particular person resource stored in the API.

- DELETE Response (Success : 204)

## Testing

- Run the file test.py in python `python test.py` to test against the publicy hosted api.
- Or alternatively run the file test_localhost.py `python test_localhost.py` to test with the localhost API you have deployed.

## Limitations

- The API does not provide authentication of any kind
- The API is very basic and only stores a person's name
