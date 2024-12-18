# Library Management System API

## Overview

This project is a simple **Library Management System API** built using Flask. It provides functionality to manage books and members, along with features such as pagination, search by title and author, and token-based authentication for securing certain operations.

---

## Table of Contents
1. [How to Run the Project](#how-to-run-the-project)
2. [Design Choices](#design-choices)
3. [Assumptions and Limitations](#assumptions-and-limitations)

---

## How to Run the Project

### Prerequisites
Before running the project, ensure you have the following:
- **Python 3.x**: The project is built using Python 3.
- **Pip**: Used to manage the project's dependencies.

### Steps to Run
1. **Clone the repository**:
   Download or clone the project repository to your local machine.

2. **Install Dependencies**:
   It's recommended to use a virtual environment to manage dependencies. After setting up the virtual environment, install the necessary Python libraries by running `pip install -r requirements.txt`.

3. **Database Setup**:
   The project uses an SQL database (SQLite by default). Ensure that the database is correctly configured, and the tables are created. The app will automatically create the necessary database and tables when you run it for the first time.

4. **Run the Flask App**:
   You can start the Flask development server by running the app file. This will launch the application, and it will be accessible on `http://127.0.0.1:5000/` in your browser or via any HTTP client (e.g., Postman).

5. **Testing the API**:
   Use an API client like Postman to interact with the API. You can test various routes such as `POST /login`, `GET /books`, and `POST /book`.

---

## Design Choices

### 1. **Flask Framework**
   - Flask is chosen for this project due to its simplicity and flexibility. It allows easy definition of RESTful routes and is well-suited for building lightweight APIs with minimal setup.

### 2. **SQLAlchemy for Database Interaction**
   - **SQLAlchemy** is used as an Object-Relational Mapping (ORM) tool, making it easier to interact with the database. It helps in abstracting SQL queries and allows us to perform CRUD operations on entities like books and members more naturally.

### 3. **Token-based Authentication**
   - For security, the API uses token-based authentication. Users must authenticate with the `/login` route to obtain a token, which must then be included in the header of requests to any protected routes (e.g., adding, updating, or deleting books).

### 4. **Pagination and Search Functionality**
   - Pagination is implemented for the `GET /books` route, which limits the number of books returned per request. Users can customize the number of items returned by specifying the `page` and `per_page` query parameters.
   - Users can also filter the books based on title or author by using search parameters in the request.

### 5. **Error Handling**
   - The application includes basic error handling using Flask’s `abort()` function. This ensures that appropriate error responses (e.g., `404 Not Found`, `401 Unauthorized`) are sent when things go wrong, such as missing tokens or invalid requests.

---

## Assumptions and Limitations

### Assumptions:
1. **Single User Authentication**:
   - The login system is hardcoded to authenticate a single user (`username: admin`, `password: password`). In a production application, this would be replaced by a more robust user authentication system such as OAuth or JWT-based authentication.

2. **In-Memory Token Storage**:
   - Tokens are stored in memory (`VALID_TOKENS`) for demonstration purposes. For a production system, token management would typically be handled with a persistent database or an external service.

3. **Database Choice**:
   - The project uses SQLite as the default database, which is lightweight and doesn’t require any additional setup. For a more scalable production environment, databases like PostgreSQL or MySQL would be more appropriate.

### Limitations:
1. **Rate Limiting and Security**:
   - The app does not implement any rate limiting or protection against brute-force attacks. These security measures would need to be added for production environments.

2. **Basic Authentication Flow**:
   - Authentication is simplified and hardcoded, providing only basic token-based authentication for a single user. In a real-world application, a full-fledged user management and authentication system would be required.

3. **Search and Filter Limitations**:
   - The search functionality only supports basic title and author filtering. More complex search features (e.g., filtering by genre, publisher, or using full-text search) are not implemented.

4. **No Input Validation**:
   - There is minimal input validation. For example, fields such as ISBN numbers or email addresses are not validated for proper formats. Input validation and error handling should be improved before deploying to production.

5. **No Advanced Features**:
   - Features like user roles (e.g., admin vs. user), book borrowing and returning, due dates, etc., are not implemented but could be added in the future.

---

## API Endpoints

### 1. **Login**
   - `POST /login`: Authenticates a user and returns a token.

### 2. **Books**
   - `GET /books`: Returns a paginated list of books with optional search by title or author.
   - `POST /book`: Adds a new book to the library.
   - `PUT /book/<id>`: Updates the details of an existing book.
   - `DELETE /book/<id>`: Deletes a book by ID.

### 3. **Members**
   - `GET /members`: Returns a list of all library members.
   - `POST /member`: Adds a new member.
   - `PUT /member/<id>`: Updates the details of an existing member.
   - `DELETE /member/<id>`: Deletes a member by ID.

---

## Conclusion

The **Library Management System API** provides basic functionality for managing books and members, implementing CRUD operations, search, pagination, and token-based authentication. While designed to be simple and extensible, the project can be expanded with additional features like user roles, advanced search, input validation, and more complex authentication schemes for a production environment.

---

