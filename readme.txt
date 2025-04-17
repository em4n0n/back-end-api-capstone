Little Lemon API - Available Endpoints for Testing

🔐 Authentication
POST /auth/users/
Create a new user account

POST /auth/token/login/
Login and retrieve an authentication token

POST /auth/token/logout/
Logout and delete the authentication token

POST /restaurant/api-token-auth
Alternate method for obtaining an authentication token

📋 Menu Items
GET /restaurant/menu/
Retrieve a list of all menu items

POST /restaurant/menu/
Add a new menu item (requires authentication)

GET /restaurant/menu/<int:pk>/
Retrieve a single menu item by ID

PUT /restaurant/menu/<int:pk>/
Update a menu item by ID (requires authentication)

DELETE /restaurant/menu/<int:pk>/
Delete a menu item by ID (requires authentication)

📅 Booking Tables
GET /restaurant/booking/tables/
View all bookings (requires authentication)

POST /restaurant/booking/tables/
Create a new table booking (requires authentication)

GET /restaurant/booking/tables/<int:pk>/
View a specific booking (requires authentication)

PUT /restaurant/booking/tables/<int:pk>/
Update a specific booking (requires authentication)

DELETE /restaurant/booking/tables/<int:pk>/
Cancel a specific booking (requires authentication)

🏠 Homepage
GET /restaurant/
Displays a simple homepage using index.html