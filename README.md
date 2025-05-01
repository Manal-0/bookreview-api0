# Book Review API
Description
This is a RESTful API built using Django and Django REST Framework (DRF) for a Book Review System. The API allows users to register, log in using JWT-based authentication, browse books, add reviews, and manage their account securely.

# How to Run the Project Locally
1. Clone the Repository
To clone the repository to your local machine, run the following command:

bash

git clone [https://github.com/yourusername/book-review-api.git](https://github.com/Manal-0/bookreview-api0.git
)
cd book-review-api
2. Set Up Virtual Environment
It's recommended to use a virtual environment to manage dependencies:

bash

python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
Install the required dependencies from requirements.txt:

bash

pip install -r requirements.txt
4. Apply Migrations
Set up the database by applying the migrations:

bash

python manage.py migrate
5. Create Superuser (Admin Access)
Create a superuser account to access the Django admin interface (optional):

bash

python manage.py createsuperuser
6. Run the Development Server
Start the development server:

bash

python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.

How to Test Each Endpoint
You can test the API endpoints using Postman or curl.

1. User Registration
Endpoint: POST /api/register/

Body:

json

{
  "username": "admin",
  "password": "123",
  "email": "admin@example.com"
}
Response:

json

{
  "message": "User registered successfully"
}
2. Login (Get JWT Token)
Endpoint: POST /api/token/

Body:

json

{
  "username": "admin",
  "password": "123"
}
Response:

json

{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
3. Get All Books
Endpoint: GET /api/books/

Headers:

text

Authorization: Bearer <your_access_token>
Response:

json

[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Author Name",
    "description": "Description of the book"
  },
  ...
]
4. Add a New Book (Admin Only)
Endpoint: POST /api/books/

Headers:

text

Authorization: Bearer <your_access_token>
Body:

json

{
  "title": "New Book Title",
  "author": "Author Name",
  "description": "Description of the book"
}
Response:

json

{
  "id": 1,
  "title": "New Book Title",
  "author": "Author Name",
  "description": "Description of the book"
}
5. Add a Review to a Book
Endpoint: POST /api/books/<book_id>/reviews/

Headers:

text

Authorization: Bearer <your_access_token>
Body:

json

{
  "rating": 5,
  "comment": "Great book!"
}
Response:

json

{
  "id": 1,
  "rating": 5,
  "comment": "Great book!",
  "created_at": "2025-05-01T00:00:00Z"
}
# Description of Authentication Mechanism Used
This API uses JWT (JSON Web Token) for user authentication and authorization.

# 1. User Registration and Login
To authenticate users, they must first register via the /api/register/ endpoint and then log in via the /api/token/ endpoint by providing a valid username and password.

After a successful login, the API returns an access token and a refresh token.

# 2. JWT Tokens
Access Token: This token is used for authenticating API requests. It should be included in the Authorization header in each API request.

Refresh Token: This token can be used to obtain a new access token when the old one expires.

# 3. Token Expiration and Refresh
The access token has a short lifespan (usually 15 minutes).

To refresh the token, users can send a request to the /api/token/refresh/ endpoint, passing the refresh token to obtain a new access token.

# 4. Securing Endpoints
The endpoints that require user authentication (like adding books or reviews) will require the Authorization header with the Bearer <access_token>.

Folder Structure
bash

book-review-api/
├── book_review/           # App for the book review functionality
│   ├── migrations/
│   ├── models.py          # Book and Review models
│   ├── serializers.py     # Serializers for the models
│   ├── views.py           # API views for books and reviews
│   ├── permissions.py     # Custom permissions for admins
├── config/                # Django project configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # URL routing
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies

# Conclusion

This Book Review API provides a secure, efficient system for users to register, log in, manage their accounts, and interact with books and reviews. The JWT authentication mechanism ensures that sensitive operations are only available to authenticated users.

For more details, feel free to browse the repository and check out the full documentation.










