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



## API Reference



###Getting Started
- Base URL: This app is yet to be hosted, hence using the `localhost` of the development machine on `port 500` 
`http://127.0.0.1:5000/` 


###Error Handling

Errors are returned as a JSON object in the format below:
```json
{
  "success": false,
  "error": "422",
  "message": "unprocessable data"
}
```

#### Endpoints

##### GET /movies

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
##### DELETE /movies/{movie_id}

* If `movie_id` exists, it deletes the given record from the database

* Sample Response:      

```json
{
    "success": true,
    "movie": 1
}
```    

##### POST /movies

* Adds a new `movie` object to the database

* Request Arguments: 

```json
  {
            "title": "Fast And Furious",
            "release_date": "11-11-2020",
  }
```   

* Sample Response:      

```json
{"message": "successful"}
```    

##### GET /categories

* Returns available `categories`

* Request Arguments: None   

* Sample Response: 

```json
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 7, 
      "type": "Technology"
    }
  ], 
  "successful": true, 
  "total_categories": 7
}

```

##### GET /categories/{category_id}/questions

* Returns all questions with given `category_id`

* Request Arguments: None   

* Sample Response: 

```json
{
  "categories": [
    {
      "id": 1, 
      "type": "Science"
    }, 
    {
      "id": 2, 
      "type": "Art"
    }, 
    {
      "id": 3, 
      "type": "Geography"
    }, 
    {
      "id": 4, 
      "type": "History"
    }, 
    {
      "id": 5, 
      "type": "Entertainment"
    }, 
    {
      "id": 6, 
      "type": "Sports"
    }, 
    {
      "id": 7, 
      "type": "Technology"
    }
  ], 
  "current_category": 1, 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "60", 
      "category": 1, 
      "difficulty": 4, 
      "id": 26, 
      "question": "How fast can a Tesla Model S go in 1.99sec"
    }, 
    {
      "answer": "60", 
      "category": 1, 
      "difficulty": 4, 
      "id": 27, 
      "question": "How fast can a Tesla Model S go in 1.99sec"
    }, 
    {
      "answer": "60", 
      "category": 1, 
      "difficulty": 4, 
      "id": 28, 
      "question": "How fast can a Tesla Model S go in 1.99sec"
    }, 
    {
      "answer": "60", 
      "category": 1, 
      "difficulty": 4, 
      "id": 29, 
      "question": "How fast can a Tesla Model S go in 1.99sec"
    }, 
    {
      "answer": "60", 
      "category": 1, 
      "difficulty": 4, 
      "id": 30, 
      "question": "How fast can a Tesla Model S go in 1.99sec"
    }
  ], 
  "successful": true, 
  "total_questions": 8
}

```



##### POST /players

* Creates new player

* Request Arguments: 

```json
{
"username": "crazychukz",
"total_score": 0
}
```   

* Sample Response: 

```json
{"success": true}
```   

##### GET /players

* Returns all players, ordered by player's score

* Request Arguments: 

```json
{
"username": "crazychukz",
"total_score": 0
}
```   

* Sample Response: 

```json
{
  "players": [
    {
      "id": 2, 
      "total_score": 4, 
      "username": "isioma"
    }, 
    {
      "id": 1, 
      "total_score": 3, 
      "username": "crazychukz"
    }, 
    {
      "id": 3, 
      "total_score": 2, 
      "username": "admin"
    }
  ], 
  "successful": true, 
  "total_players": 3
}

``` 

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


## Appreciation

* Udacity Instructor
* Katherine Kato - https://codepen.io/kathykato for the free 3D button