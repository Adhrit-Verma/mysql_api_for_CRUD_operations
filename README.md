# User API

This is a simple API built with Flask that allows users to perform CRUD operations on a MySQL database for managing user information.

## Setup

1. Install the required packages by running the following command:

pip install Flask mysql-connector-python

2. Create a MySQL database with the name 'users' using your preferred MySQL client.

3. Modify the database connection details in the `db_config` dictionary in the code (`app.py`) to match your MySQL server configuration (host, user, password).

4. Run the following command to start the Flask application:

python app.py

The API will run on http://localhost:5000 by default.

## Endpoints

The API provides the following endpoints:

- `GET /users` - Retrieve a list of all users.
- `GET /users/{id}` - Retrieve details of a specific user.
- `POST /users` - Create a new user.
- `PUT /users/{id}` - Update details of a specific user.
- `DELETE /users/{id}` - Delete a specific user.

## Usage

You can use tools like cURL or Postman to interact with the API endpoints. Here are some examples:

- Retrieve all users:

GET /users

- Retrieve details of a specific user:

GET /users/{id}

- Create a new user:

POST /users
{
"user_name": "john_doe",
"password": "password123",
"phone": "1234567890"
}

- Update details of a specific user:

PUT /users/{id}
{
"user_name": "new_username",
"password": "new_password",
"phone": "9876543210"
}

- Delete a specific user:

DELETE /users/{id}

Please adjust the endpoint URLs and request payloads according to your setup and requirements.

## Error Handling

If any error occurs during the API requests or database operations, appropriate error messages and status codes will be returned in the response.

