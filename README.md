# FSND - Capstone API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. 
Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend micro-services framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the capstone.psql file provided. From the backend folder in terminal run:
```bash
psql capstone < capstone.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## RBAC controls  :unlock:




## API Reference



### Getting Started

- Base URL: This app is yet to be hosted, hence using the `localhost` of the development machine on `port 500` 
`http://127.0.0.1:5000/` 


### Error Handling

Errors are returned as a JSON object in the format below:
```json
{
  "success": false,
  "error": "422",
  "message": "unprocessable data"
}
```

### Movies Endpoints

### GET /movies

* Returns list of added movies 

* Sample Response: 

```json
{
    "movies": [
        {
            "casts": [
                {
                    "id": 1,
                    "name": "Emeka Charles"
                }
            ],
            "id": 1,
            "release_date": "Wed, 11 Nov 2020 00:00:00 GMT",
            "title": "Fast And Furious"
        },
        {
            "casts": [
                {
                    "id": 1,
                    "name": "Emeka Charles"
                }
            ],
            "id": 3,
            "release_date": "Tue, 01 Dec 2020 00:00:00 GMT",
            "title": "Aki Na Ukwa"
        },
        {
            "casts": [],
            "id": 5,
            "release_date": "Tue, 01 Dec 2020 00:00:00 GMT",
            "title": "Aki Na Ukwa Two"
        },
        {
            "casts": [],
            "id": 6,
            "release_date": "Tue, 01 Dec 2020 00:00:00 GMT",
            "title": "Aki Na Ukwa Three"
        },
        {
            "casts": [],
            "id": 7,
            "release_date": "Tue, 01 Dec 2020 00:00:00 GMT",
            "title": "Aki Na Ukwa Four"
        },
        {
            "casts": [],
            "id": 8,
            "release_date": "Tue, 01 Dec 2020 00:00:00 GMT",
            "title": "Aki Na Ukwa Five"
        },
        {
            "casts": [
                {
                    "id": 1,
                    "name": "Emeka Charles"
                }
            ],
            "id": 9,
            "release_date": "Tue, 01 Dec 2020 00:00:00 GMT",
            "title": "Aki Na Ukwa Six"
        }
    ],
    "success": true,
    "total": 7
}

```
### DELETE /movies/{movie_id}

* If `movie_id` exists, it deletes the given record from the database

* Sample Response:      

```json
{
    "success": true,
    "movie": 1
}
```    

### POST /movies

* Adds a new `movie` object to the database

* Request Arguments: 

```json
  {
            "title": "Fast And Furious",
            "release_date": "11-11-2020"
  }
```   

* Sample Response:      

```json
{
    "movie": [
        {
            "casts": [],
            "id": 10,
            "release_date": "Wed, 11 Nov 2020 00:00:00 GMT",
            "title": "Fast And Furious"
        }
    ],
    "success": true
}
```  

### PATCH /movies/{movie_id}

* If `movie_id` exists, it updates the given record on the database


* Request Arguments: 

```json
  {
            "title": "Fast And Furious 2",
  }
``` 

* Sample Response:      

```json
{
    "movie": [
        {
            "casts": [
                {
                    "id": 1,
                    "name": "Fast And Furious 2"
                }
            ],
            "id": 1,
            "release_date": "Wed, 11 Nov 2020 00:00:00 GMT",
            "title": "Tom Guy"
        }
    ],
    "success": true
}
```  
  

### Actors Endpoints

### GET /actors

* Returns available `actors`

* Request Arguments: None   

* Sample Response: 

```json

{
    "actors": [
        {
            "id": 1,
            "name": "Thomas Cruise"
        }
    ],
    "success": true,
    "total": 1
}

```

### POST /actors

* Creates new `actor` record in the database

* Request Arguments: 

```json
{
    "name": "Thomas Cruise",
    "gender": "Male",
    "age": "45"
}
```   

* Sample Response: 

```json
{
    "actor": [
        {
            "age": 45,
            "gender": "Male",
            "id": 2,
            "name": "Thomas Cruise"
        }
    ],
    "success": true
}
```   



## Running Tests

To run the tests
```
$ dropdb capstone_test
```
```
$ createdb capstone_test
```
```
$ psql capstone_test < trivia.psql
 ```
 ```
$ python test_app.py
```


## Appreciation

* Udacity Instructors
