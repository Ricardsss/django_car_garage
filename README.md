Car Garage API

This API allows you to manage cars in a car garage system. It supports creating, updating, retrieving, and deleting car records, as well as retrieving all cars or a specific car by its ID.

Endpoints

1. Create a New Car (POST /cars/)
   Description:

Creates a new car record.

Request Method:

POST

URL:

/cars/

Request Body:

json
Copy code
{
"car_model": "<car_model_id>", # UUID of the CarModel object
"colour": "string", # Colour of the car
"year": "YYYY", # Year of manufacture (4 characters)
"VIN": "17-char VIN", # Vehicle Identification Number (17 characters)
"mileage": integer, # Mileage of the car
"status": "a" # Car rental status ('a' = Available, 'u' = Unavailable, 'm' = Maintenance)
}
Response:

201 Created: The car was successfully created.
400 Bad Request: Invalid input or VIN already exists.
Example:

bash
Copy code
curl -X POST http://localhost:8000/cars/ \
-H "Content-Type: application/json" \
-d '{
"car_model": "123e4567-e89b-12d3-a456-426614174000",
"colour": "Red",
"year": "2020",
"VIN": "1HGCM82633A123456",
"mileage": 15000,
"status": "a"
}' 2. Get All Cars (GET /cars/)
Description:

Retrieves a list of all cars in the system.

Request Method:

GET

URL:

/cars/

Response:

200 OK: A list of cars is returned.
500 Internal Server Error: An error occurred while fetching the data.
Example:

bash
Copy code
curl -X GET http://localhost:8000/cars/
Response:

json
Copy code
[
{
"id": "c84a3e7b-7e1e-4211-89a6-d3b0243fe2b4",
"car_model": "Toyota Camry",
"colour": "Red",
"year": "2020",
"VIN": "1HGCM82633A123456",
"mileage": 15000,
"status": "Available"
},
...
] 3. Get Car by ID (GET /cars/<uuid:car_id>/)
Description:

Retrieves details of a single car by its ID.

Request Method:

GET

URL:

/cars/<uuid:car_id>/

Response:

200 OK: The car details are returned.
404 Not Found: Car not found.
Example:

bash
Copy code
curl -X GET http://localhost:8000/cars/c84a3e7b-7e1e-4211-89a6-d3b0243fe2b4/
Response:

json
Copy code
{
"id": "c84a3e7b-7e1e-4211-89a6-d3b0243fe2b4",
"car_model": "Toyota Camry",
"colour": "Red",
"year": "2020",
"VIN": "1HGCM82633A123456",
"mileage": 15000,
"status": "Available"
} 4. Update Car (PATCH /cars/<uuid:car_id>/)
Description:

Updates a car's details partially.

Request Method:

PATCH

URL:

/cars/<uuid:car_id>/

Request Body:

You can send any of the following fields to update:

json
Copy code
{
"car_model": "<car_model_id>", # UUID of the CarModel object
"colour": "string", # Colour of the car
"year": "YYYY", # Year of manufacture (4 characters)
"VIN": "17-char VIN", # Vehicle Identification Number (17 characters)
"mileage": integer, # Mileage of the car
"status": "a" # Car rental status ('a' = Available, 'u' = Unavailable, 'm' = Maintenance)
}
Response:

200 OK: The car was successfully updated.
404 Not Found: Car not found.
400 Bad Request: Invalid input.
Example:

bash
Copy code
curl -X PATCH http://localhost:8000/cars/c84a3e7b-7e1e-4211-89a6-d3b0243fe2b4/ \
-H "Content-Type: application/json" \
-d '{
"colour": "Green",
"mileage": 16000
}' 5. Delete Car (DELETE /cars/<uuid:car_id>/)
Description:

Deletes a specific car by its ID.

Request Method:

DELETE

URL:

/cars/<uuid:car_id>/

Response:

200 OK: The car was successfully deleted.
404 Not Found: Car not found.
Example:

bash
Copy code
curl -X DELETE http://localhost:8000/cars/c84a3e7b-7e1e-4211-89a6-d3b0243fe2b4/
Response:

json
Copy code
{
"message": "Car deleted successfully"
}
Status Codes

200 OK: Successful requests.
201 Created: The resource was successfully created.
400 Bad Request: The input data is invalid.
404 Not Found: The requested resource does not exist.
405 Method Not Allowed: The HTTP method used is not allowed.
500 Internal Server Error: An unexpected server error occurred.
Setup

To run this project locally:

Clone the repository.
Run "cd cargarage"
Install the required dependencies using pip install -r requirements.txt.
Set up the database using python manage.py migrate.
Run the development server using python manage.py runserver.
Notes

Ensure proper validation is in place for creating and updating cars.
For PATCH and DELETE requests, ensure that only authorized users have access to these actions in production.
