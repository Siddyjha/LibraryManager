# Packages

django = "*" <br>
djangorestframework = "*" <br>

# Requires

python_version = "3.8" <br>

# Installation

Upgrade pip

`python -m pip install --upgrade pip`
    
Install pipenv

    pip install pipenv
    
Clone Respository

```git clone https://github.com/Siddyjha/LibraryManager.git```

```cd LibraryManager```
   
In LibraryManager/

    pipenv shell
    
Install Dependencies

    pipenv install
    
Move to Django Project Dir
    
```cd LibraryManager```
    
In /LibraryManager/LibraryManager/

    python manage.py runserver
    
The Backend is now running on ```http://localhost:8000/```

Use an application like POSTMAN to test API
   

# API Documentation

### Student
* Get list of books available for issuing.

    ```http://localhost:8000/api/book/student/list```
    
    Response:

    ```
    [
        {
            "bookID": "b01",
            "name": "A Brief History Of TIme",
            "isIssued": false
        },
        {
            "bookID": "b02",
            "name": "I Feel Bad About My Neck",
            "isIssued": false
        }
    ]
    ```
* Issue a book

    ```http://localhost:8000/api/book/student/issue```
    
    POST request with body
    
    ```
    {
      "bookID":"b010",
      "studID":"s1"
    }
    ```
    
    Response
    
    ```
    {
      "bookID": "b010",
      "name": "The Siege",
      "isIssued": true
    }
    ```
    
* Return Book

    ```http://localhost:8000/api/book/student/return```
    
    POST request with body
    
    ```
    {
      "bookID":"b010",
      "studID":"s1"
    }
    ```
    
    Response
    
    ```
    {
      "bookID": "b010",
      "name": "The Siege",
      "isIssued": false
    }
    ```
    
* Request Access To Issued Book

    ```http://localhost:8000/api/book/student/access_request```
    
    POST request with body
    
    ```
    {
      "bookID":"b015",
      "studID":"s1"
    }
    ```
    
    Response
    
    ```
    {
      "bookID": "b015",
      "studID": "s1"
    }
    ```
    
### Librarian

* Get All Books In Library
    
    ```http://localhost:8000/api/book/librarian/list```
    
    Response
    
    ```
    [
      {
          "bookID": "b01",
          "name": "A Brief History Of TIme",
          "isIssued": false
      },
      {
          "bookID": "b02",
          "name": "I Feel Bad About My Neck",
          "isIssued": false
      },
      {
          "bookID": "b03",
          "name": "Broken Glass",
          "isIssued": false
      }
    ]
    ```
    
* Get All Access Requests

    ```http://localhost:8000/api/book/librarian/list_access_req```
    
    Response
    
    ```
    [
      {
          "bookID": "b01",
          "studID": "s1"
      },
      {
          "bookID": "b015",
          "studID": "s1"
      },
      {
          "bookID": "b015",
          "studID": "s1"
      }
    ] 
    ```
