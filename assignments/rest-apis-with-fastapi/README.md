# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using the FastAPI framework. In this assignment, you will practice creating API routes, returning JSON data, and handling basic create and lookup operations.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application for a small book collection. Your API should include routes that let a user check that the server is running and view book data.

#### Requirements
Completed program should:

- Create a FastAPI application.
- Add a route for `/` that returns a short welcome message.
- Add a route for `/books` that returns a list of books as JSON.
- Add a route for `/books/{book_id}` that returns one book when the id exists.
- Return a clear message if a requested book id is not found.

Example response:

```json
{
  "id": 1,
  "title": "Python Basics",
  "author": "M. Lee",
  "in_stock": true
}
```

### 🛠️ Add Create and Delete Features

#### Description
Expand the API so users can add new books and remove existing ones. Use FastAPI request handling to accept JSON input and update the in-memory book list.

#### Requirements
Completed program should:

- Add a `POST /books` route that accepts a new book in JSON format.
- Store the new book in the in-memory list.
- Add a `DELETE /books/{book_id}` route that removes a book when the id exists.
- Return a success message after creating or deleting a book.
- Keep the API responses in valid JSON format.

Example request body:

```json
{
  "id": 3,
  "title": "Web APIs for Beginners",
  "author": "A. Smith",
  "in_stock": true
}
```