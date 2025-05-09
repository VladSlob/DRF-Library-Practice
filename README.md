# DRF-Library-Practice (Vladyslav Slobodian)

# Library Service
Description:

This is an API service built with Django REST Framework (DRF) for managing a library. It's designed for local library management, handling books, borrowing transactions, and payments.

Tasks:
1. Enable CRUD operations for the Books Service.
   - Initialize the 'books' application.
   - Add the 'Book' model.
   - Implement the serializer and views for all endpoints.

2. Enable CRUD operations for the Users Service.
   - Initialize the 'users' application.
   - Add the 'User' model including an email field.
   - Implement JWT (JSON Web Token) support.
   - For improved usability with the ModHeader Chrome extension, change the default 'Authorization' header for JWT authentication to something like 'Authorize'. Refer to the documentation for implementation details.
   - Implement the serializer and views for all endpoints.

3. Implement permission controls for the Books Service.
   - Only administrator users should have the permission to create, update, and delete books.
   - All users, including those who are not logged in, should be able to view the list of books.
   - Implement JWT token authentication provided by the users service to manage permissions.
