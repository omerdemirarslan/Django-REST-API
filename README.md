## Django-REST-API

### Project Explaning:

This project is built using the Django framework and Django REST framework libraries. Apart from these, the project is
dockerized with the docker application. When you download the project to your local, for you to deal with extra database
operations; SQLite3 database, which is Django's default database, is used. You don't need migrate for models; docker
make it for you.

* This project name: **Arena**
* This project have one app: **Gamers**

### Required Application:

For the project to up; Docker application must be installed and running in your local.

### Install Project:

    git clone https://github.com/omerdemirarslan/Django-REST-API

### Run The Project:

    docker-compose up

### In Browser:

    localhost/

### API Endpoints:

    * /users/sign-up/                   (User Registration Endpoint)
    * /users/me/                        (User Login Endpoint)
    * /users/search/?keyword=<keyword>  (User Search Endpoint)
    * /users/update/                    (User Update Endpoint)

### Test Case Scenarios:

* Sign up a user with API
* Login a user with API
* Search a user with API
* Update a user with API
* Test to register with mismatched password.
* Test to verify registration with already exists username.
* Test to verify registration with valid datas
* Tested API authentication endpoint validations

### Endpoints

#### Sign Up

* **URL:** `/users/sign-up/`
* **METHOD:** `POST`

#### Request

```json
{
  "user": {
    "first_name": "Tony",
    "last_name": "STARK",
    "username": "iron-man",
    "email": "ironman@gmail.com",
    "password": "peperlove",
    "confirm_password": "peperlove"
  },
  "birthdate": "02.05.2008",
  "about": "The truth is I'm iron man"
}
```

#### Response

```json
{
  "id": 11
}
```

---

#### Login

* **URL:** `/users/me/`
* **METHOD:** `POST/GET`

#### Request

    username: iron-man
    password: peperlove

#### Response

```json
{
  "about": "The truth is I'm iron man",
  "birthdate": "02.05.2008",
  "date_joined": "2021-07-09T22:32:29.183918Z",
  "first_name": "Tony",
  "last_name": "STARK"
}
```

---

#### Search

* **URL:** `/users/search/`
* **METHOD:** `GET`

#### Request

    /users/search/?username=iron-man

#### Response

```json
[
  {
    "id": 11,
    "user_name": "iron-man",
    "first_name": "Tony",
    "last_name": "STARK",
    "about": "The truth is I'm iron man",
    "birthdate": "02.05.2008"
  }
]
```

---

#### Update

* **URL:** `/users/update/`
* **METHOD:** `PUT/PATCH`

#### Request

```json
{
  "birthdate": "26.04.2019",
  "about": "I love you 3000"
}
```

#### Response

```json
{
  "birthdate": "26.04.2019",
  "about": "I love you 3000"
}
```

---
---

### Last Notes:

My project is always open to development. I admit it's not perfect, but my goal is not to be perfect, but to always be
able to do better. I am waiting for your positive or negative feedback.


---
---
