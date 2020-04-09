# App Docs
The app folder is the root folder for the project. There are multimple settings files in respect to the environment you will want to run it. [prod/dev]

# Application Flow

1. An author registers onto the platform
   1.1 The author can be performed CRUD with admin previlages.
2. Author can create a blog.
   2.1 Author can perform CRUD on blog item attectched to the instance. 

# API Docs
This is the available APIS that can be tested using Postman/Insomnia

## Account API's
This are the CRUD API's for account app.

1. CREATE AUTHOR:
PROTOCOL:   [POST]
URI:        http://127.0.0.1:8000/api/v1/account/signup/
PAYLOAD:    {
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@gmail.com",
                "active": true
            }
RESPONSE:   {
                "status": "200",
                "data": {
                    "url": "/api/v1/account/1/",
                    "slug": "",
                    "pk": 1,
                    "user": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "johndoe@gmail.com",
                    "active": true,
                    "timestamp": "2020-04-09T00:56:54.904747+03:00",
                    "updated": "2020-04-09T00:56:54.919041+03:00"
                },
                "message": "Succesfully Created Author"
            }

2. LIST AUTHOR:
PROTOCOL:   [GET]
URI:        http://127.0.0.1:8000/api/v1/account/
RESPONSE:   [
                {
                    "url": "http://127.0.0.1:8000/api/v1/account/1/",
                    "slug": "john",
                    "pk": 1,
                    "user": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "johndoe@gmail.com",
                    "active": true,
                    "timestamp": "2020-04-08T23:43:37.056024+03:00",
                    "updated": "2020-04-09T01:06:15.439707+03:00"
                }
            ]

3. AUTHOR DETAILS:
PROTOCOL:   [GET]
URI:        http://127.0.0.1:8000/api/v1/account/1/
RESPONSE:   {
                "status": "200",
                "message": "Found john",
                "data": {
                    "url": "/api/v1/account/1/",
                    "slug": "john",
                    "pk": 1,
                    "user": 1,
                    "first_name": "John",
                    "last_name": "Doe",
                    "email": "johndoe@gmail.com",
                    "active": true,
                    "timestamp": "2020-04-08T23:43:37.056024+03:00",
                    "updated": "2020-04-09T01:04:36.565520+03:00"
                }
            }

4. AUTHOR UPDATE:
PROTOCOL:   [PUT]
URI:        http://127.0.0.1:8000/api/v1/account/1/
PAYLOAD:    {
                "first_name": "Geoffrey",
                "last_name": "Mahugu",
                "email": "geoffreymahugu@gmail.com",
                "active": true
            }
RESPONSE:   {
                "status": "200",
                "data": {
                    "url": "/api/v1/account/1/",
                    "slug": "john",
                    "pk": 1,
                    "user": 1,
                    "first_name": "Geoffrey",
                    "last_name": "Mahugu",
                    "email": "geoffreymahugu@gmail.com",
                    "active": true,
                    "timestamp": "2020-04-08T23:43:37.056024+03:00",
                    "updated": "2020-04-09T01:06:15.439707+03:00"
                },
                "message": "Succesfully Updated Author"
            }

5. AUTHOR DELETE:
PROTOCOL:   [DELETE]
URI:        http://127.0.0.1:8000/api/v1/account/1/
RESPONSE:   {
                "status": "200",
                "message": "DELETED geoff",
                "data": {
                    "url": "/api/v1/account/1/",
                    "slug": "geoff",
                    "pk": 1,
                    "user": 1,
                    "first_name": "Geoffrey",
                    "last_name": "Mahugu",
                    "email": "geoffreymahugu@gmail.com",
                    "active": false,
                    "timestamp": "2020-04-08T23:43:37.056024+03:00",
                    "updated": "2020-04-09T01:06:03.679975+03:00"
                }
            }

## Blog API's
This are the CRUD API's for blog app.

1. CREATE BLOG:
PROTOCOL:   [POST]
URI:        http://127.0.0.1:8000/api/v1/blog/create/1/
PAYLOAD:    {
                "title": "Title Header",
                "body": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
            }
RESPONSE:   {
                "status": "200",
                "data": {
                    "url": "/api/v1/blog/1/",
                    "pk": 1,
                    "author": 1,
                    "title": "Title Header",
                    "body": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
                    "timestamp": "2020-04-09T01:56:08.849801+03:00",
                    "updated": "2020-04-09T01:56:08.849839+03:00"
                },
                "message": "Succesfully Created Article"
            }

2. GET BLOGS:
PROTOCOL:   [GET]
URI:        http://127.0.0.1:8000/api/v1/blog/
RESPONSE:   [
                {
                    "url": "http://127.0.0.1:8000/api/v1/blog/1/",
                    "pk": 1,
                    "author": 1,
                    "title": "Title Header",
                    "body": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
                    "timestamp": "2020-04-09T01:46:03.909025+03:00",
                    "updated": "2020-04-09T01:46:03.909061+03:00"
                },
            ]

3. BLOG DETAILS:
PROTOCOL:   [GET]
URI:        http://127.0.0.1:8000/api/v1/blog/1/
RESPONSE:   {
                "status": "200",
                "message": "Title Header",
                "data": {
                    "url": "/api/v1/blog/1/",
                    "pk": 1,
                    "author": 1,
                    "title": "Title Header",
                    "body": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
                    "timestamp": "2020-04-09T01:44:47.006435+03:00",
                    "updated": "2020-04-09T01:44:47.006461+03:00"
                }
            }

3. BLOG UPDATE:
PROTOCOL:   [PUT]
URI:        http://127.0.0.1:8000/api/v1/blog/1/
PAYLOAD:    {
                "title": "UPDATED: Title Header",
                "body": "UPDATED: It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
            }
RESPONSE:   {
                "status": "200",
                "message": "UPDATED: Title Header",
                "data": {
                    "url": "/api/v1/blog/1/",
                    "pk": 1,
                    "author": 1,
                    "title": "UPDATED: Title Header",
                    "body": "UPDATED: It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
                    "timestamp": "2020-04-09T01:44:47.006435+03:00",
                    "updated": "2020-04-09T01:44:47.006461+03:00"
                }
            }

3. BLOG DELETE:
PROTOCOL:   [DELETE]
URI:        http://127.0.0.1:8000/api/v1/blog/1/
RESPONSE:   {
                "status": "200",
                "message": "DELETED: Title Header",
                "data": {
                    "url": "/api/v1/blog/1/",
                    "pk": 1,
                    "author": 1,
                    "title": "Title Header",
                    "body": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
                    "timestamp": "2020-04-09T01:44:47.006435+03:00",
                    "updated": "2020-04-09T02:02:02.399919+03:00"
                }
            }
