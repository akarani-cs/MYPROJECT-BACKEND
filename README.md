# MYPROJECT-BACKEND
This is my ALX project back end


i'll use django and django rest framework.

This API is a Django REST Framework (DRF) project that allows users to create, read, update, and delete (CRUD) reviews for movies. It also includes user management with authentication and permissions. The API demonstrates backend development skills in database design, authentication, authorization, search, filtering, and deployment.

Authentication

Register, login, JWT authentication

Only authenticated users can create, update, or delete their own reviews

Review Management (CRUD)

Movie Title, Review Content, Rating (1–5), User, Created Date

Validation for required fields

Permissions

Users can only edit or delete their own reviews

Admins can manage all users and reviews

Search, Filtering & Pagination

Search reviews by movie title or content

Filter reviews by rating

Sort by rating or created date

Paginated results (10 per page)

Endpoints for Reviews by Movie

/api/reviews/by-movie/?title=Inception