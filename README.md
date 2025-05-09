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

4. Create the Borrowing List endpoint to display all borrowing activities and a Borrowing Detail endpoint to show information for a specific borrowing.
   - Initialize the 'borrowings' application.
   - Add the 'Borrowing' model, including constraints for borrow_date, expected_return_date, and actual_return_date.
   - Implement a read serializer that includes detailed book information.
   - Implement the list and detail endpoints.

5. Create the endpoint to handle the process of borrowing a book.
   - Implement a create serializer.
   - Validate that the book inventory is greater than zero.
   - Reduce the book inventory by one.
   - Associate the currently logged-in user with the borrowing record.
   - Implement the create endpoint.

6. Add functionality to filter the results of the Borrowings List endpoint.
   - Ensure that non-admin users can only view their own borrowing records.
   - Restrict access to borrowing information to authenticated users only.
   - Implement an is_active parameter to filter borrowings by their status (i.e., whether they are still active/not returned).
   - For admin users, add a user_id parameter: if specified, it filters borrowings for that specific user; if not, it displays all users' borrowings.

7. Design and implement the feature that enables the return of borrowed books.
   - Ensure that a borrowing cannot be returned more than once.
   - Increase the book's inventory by one upon return.
   - Implement an endpoint for handling book returns.

8. Create the Payments List endpoint to display all payment transactions and a Payment Detail endpoint to show information for a specific payment.
   - This task serves as a straightforward introduction to the payments functionality within the system.
   - Create the 'Payment' model.
   - Create the serializer and views for the list and detail endpoints.
   - Ensure that non-admin users can only view their own payments, while administrators can view all payments.

Installing using GitHub:

Python 3 needs to be installed beforehand.

How to use it:

1. Download the code
```
$ # Get the code
$ git clone https://github.com/VladimirDolhyi/library.git
$ cd library_api
```

Set Up:
Install modules via VENV
