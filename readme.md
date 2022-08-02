# Books api

## Getting Started

### Installing Dependencies

### Python 3.10.4

### pip 22.1.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

### Follow instructions to install the latest version of python for your platform in the https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/apibooks` directory and running:

```sh
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file

##### Key Dependencies

- https://flask.palletsprojects.com/en/2.1.x/ -Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- https://www.sqlalchemy.org/ - SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
- https://flask-cors.readthedocs.io/en/latest/# - Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

# Database Setup

With Postgres running, this command in the terminal to connect to Postgres

```sh
psql -U postgres
then
Password for postgres user: Your password here
```

. From the backend folder in terminal run:

```sh
flask db init
then
flask db migrate
finally
flask db upgrade
```

to execute the migrations.

# auth0

First you log in to the site of auth0.com and create an account on the site.You create a domain name. After you create an api in api in the create domain. In the parameters you must check:

```sh
Enable RBAC
Add Permissions in the Access Token
Allow Skipping User Consent
```

In permissions you must add the following permissions

```sh
get:livres
get:livre
get:categories
get:categorie
get:livres_categprie
post:livre
post:categorie
delete:livre
delete:categorie
patch:livre
patch:categorie
```

You go to applications in the domain and then create the application that will have the same name as the api create previously without forgetting to check the permissions create before.
In test folder copy this:

```sh
curl --request POST \
  --url YOUR URL \
  --header 'content-type: application/json' \
  --data '{"client_id":YOUR CLIENT_ID,"client_secret":CLIENT_SECRET,"audience":YOUR AUDIENCE,"grant_type":"client_credentials"}'
```

and run it in the terminal
YOU have the response like this

```sh
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IldZLWFOZzRsQ1dBZjJjY253Nk1nXyJ9.eyJpc3MiOiJodHRwczovL2Vzc29sYWtpbmEuZXUuYXV0aDAuY29tLyIsInN1YiI6IlNZUHlLMHBDUTRQYTBEa09yb0hzNUY2dTU5Mm00dzR3QGNsaWVudHMiLCJhdWQiOiJhcGlib29rcyIsImlhdCI6MTY1OTE3OTE5NiwiZXhwIjoxNjU5MjY1NTk2LCJhenAiOiJTWVB5SzBwQ1E0UGEwRGtPcm9IczVGNnU1OTJtNHc0dyIsInNjb3BlIjoiZ2V0OmxpdnJlcyBnZXQ6bGl2cmUgZ2V0OmNhdGVnb3JpZXMgZ2V0OmNhdGVnb3JpZSBkZWxldGU6bGl2cmUgZGVsZXRlOmNhdGVnb3JpZSBwb3N0OmxpdnJlIHBvc3Q6Y2F0ZWdvcmllIHBhdGNoOmxpdnJlIHBhdGNoOmNhdGVnb3JpZSBnZXQ6bGl2cmVzX2NhdGVnb3JpZSIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpsaXZyZXMiLCJnZXQ6bGl2cmUiLCJnZXQ6Y2F0ZWdvcmllcyIsImdldDpjYXRlZ29yaWUiLCJkZWxldGU6bGl2cmUiLCJkZWxldGU6Y2F0ZWdvcmllIiwicG9zdDpsaXZyZSIsInBvc3Q6Y2F0ZWdvcmllIiwicGF0Y2g6bGl2cmUiLCJwYXRjaDpjYXRlZ29yaWUiLCJnZXQ6bGl2cmVzX2NhdGVnb3JpZSJdfQ.kHmPdyg-ViVHqMGv3IxLqJuAUcNS4AFcEi_GgWr-Anh5tzApANd6vwHg5nca_eKOaQvNLeZfc-UGKNs0k5gSC_TprIGgCfI_rwCIjT0v0NkF9XD99w26rCaEL2Gtre7TOYZS3UZYGoeFxDLPZ2WUnpSUo_RsZwNvpVIwVeA0jUjuQ_aBd8P-U3khlBXEKnAWm8hCvwV85AWDUfeY9dEtmLfUX2v9CmbpCW7bICs6Nx2sAdulAjNUSgNoUdz_QYylEIyp1-UxXYkApPRhY7AcisXLcQXo5cUADW1JgKtbQRyQylv5sWmu5o2FADp7av4mcwfaaofHwhV2r3kUleMS9w",
  "token_type": "Bearer"
}
```
# .env

From the backend folder create this file .env and put all this command in the file

```sh
FLASK_APP=app.py
FLASK_ENV=development
motdepasse=Your password
SECRET_KEY=2de22e17383f48db7052a3fe5e34d2248eb21b5b08f3bc173d3c924d7571f6b0

AUTH0_DOMAIN=YOUR AUTH0_DOMAIN
API_AUDIENCE =YOUR API_AUDIENCE
client_id= YOUR client_id
client_secret= YOUR client_secret
```

# Running the server

From within the `booksapi` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```sh
flask run
```

# API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

# Error Handling

Errors are retourned as JSON objects in the following format:`{ "success":False "error": 400 "message":"Bad request }`

The API will return four error types when requests fail:`. 400: Bad request . 500: Internal server error . 422: Unprocessable . 404: Not found`

# Endpoints

. ## GET/livres

```sh
GENERAL:
    This endpoints returns a list of plant object, success value, total number of the books.


SAMPLE: curl http://localhost:5000/livres
{
    "livres": [
        {
            "categorie_id": 1,
            "dateparution": "Thu, 05 Feb 1998 00:00:00 GMT",
            "editeur": "editeur1",
            "id": 1,
            "isbn": "isbn1",
            "titre": "titre1",
            "version": "version1"
        },
        {
            "categorie_id": 1,
            "dateparution": "Sun, 05 Aug 1990 00:00:00 GMT",
            "editeur": "editeur2",
            "id": 2,
            "isbn": "isbn2",
            "titre": "titre2",
            "version": "version1"
        },
        {
            "categorie_id": 1,
            "dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
            "editeur": "editeur3",
            "id": 3,
            "isbn": "isbn3",
            "titre": "titre3",
            "version": "version1"
        },
        {
            "categorie_id": 2,
            "dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
            "editeur": "editeur4",
            "id": 4,
            "isbn": "isbn4",
            "titre": "titre4",
            "version": "version1"
        },
        {
            "categorie_id": 1,
            "dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
            "editeur": "editeur5",
            "id": 5,
            "isbn": "isbn5",
            "titre": "titre5",
            "version": "version2"
        }
    ],
    "nombre_livre": 5
}
```

```

. ## DELETE/livres (livre_id)

    GENERAL:
        Delete the book of the given ID if it exists. Return the id of the deleted book, success value, total of books a
.

        SAMPLE: curl -X DELETE http://localhost:5000/livre/5
        "deleted_id":5
        {
    "id": "5",
    "livres": [
        {
            "categorie_id": 1,
            "dateparution": "Thu, 05 Feb 1998 00:00:00 GMT",
            "editeur": "editeur1",
            "id": 1,
            "isbn": "isbn1",
            "titre": "titre1",
            "version": "version1"
        },
        {
            "categorie_id": 1,
            "dateparution": "Sun, 05 Aug 1990 00:00:00 GMT",
            "editeur": "editeur2",
            "id": 2,
            "isbn": "isbn2",
            "titre": "titre2",
            "version": "version1"
        },
        {
            "categorie_id": 1,
            "dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
            "editeur": "editeur3",
            "id": 3,
            "isbn": "isbn3",
            "titre": "titre3",
            "version": "version1"
        },
        {
            "categorie_id": 2,
            "dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
            "editeur": "editeur4",
            "id": 4,
            "isbn": "isbn4",
            "titre": "titre4",
            "version": "version1"
        }
    ],
    "message": "Suppression effectuée avec succès",
    "nombre_livre": 4
}
```

````sh
. ##PATCH/livres(livre_id)
  GENERAL:
  This endpoint is used to update a version of plant
  We return a plant which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/plants/1 -H "Content-Type:application/json" -d "{"version":"version2"}"
  {
    "id": 1,
    "livre": {
        "categorie_id": 1,
        "dateparution": "Thu, 05 Feb 1998 00:00:00 GMT",
        "editeur": "editeur1",
        "id": 1,
        "isbn": "isbn1",
        "titre": "titre1",
        "version": "version2"
    },
    "message": "Modification effectuée avec succès"
}
````

```
. ## POST/livres
  GENERAL:
We return the ID of the new book created, the plant that was created, the list of book and the number of books
```
with postman we have
{
"isbn":"isbn5",
"titre":"titre5",
"editeur":"editeur5",
"dateparution":"1990-08-01",
"version":"version2",
"categorie_id":1
}
response
{
"id": 6,
"livres": [
{
"categorie_id": 1,
"dateparution": "Sun, 05 Aug 1990 00:00:00 GMT",
"editeur": "editeur2",
"id": 2,
"isbn": "isbn2",
"titre": "titre2",
"version": "version1"
},
{
"categorie_id": 1,
"dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
"editeur": "editeur3",
"id": 3,
"isbn": "isbn3",
"titre": "titre3",
"version": "version1"
},
{
"categorie_id": 2,
"dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
"editeur": "editeur4",
"id": 4,
"isbn": "isbn4",
"titre": "titre4",
"version": "version1"
},
{
"categorie_id": 1,
"dateparution": "Thu, 05 Feb 1998 00:00:00 GMT",
"editeur": "editeur1",
"id": 1,
"isbn": "isbn1",
"titre": "titre1",
"version": "version2"
},
{
"categorie_id": 1,
"dateparution": "Wed, 01 Aug 1990 00:00:00 GMT",
"editeur": "editeur5",
"id": 6,
"isbn": "isbn5",
"titre": "titre5",
"version": "version2"
}
],
"nombre_livre": 5
}

```


