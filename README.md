# Car Garage API

This API allows you to manage cars, car models, and car makes. The available endpoints are as follows:

## Endpoints

### 1. Get All Cars

- **URL**: `/cars/`
- **Method**: GET
- **Description**: Retrieves a list of all cars in the system.
- **Request Body**: None

### 2. Create a New Car

- **URL**: `/cars/`
- **Method**: POST
- **Description**: Creates a new car. If the car model and make do not exist, they will be created.
- **Request Body Example**:

```json
{
  "make_name": "Honda",
  "model_name": "Civic",
  "colour": "Blue",
  "year": "2021",
  "VIN": "1HGCM82633A123457",
  "mileage": 12000
}
```

### 3. Get a Car by ID

- **URL**: `/cars/<uuid:car_id>/`
- **Method**: GET
- **Description**: Retrieves the details of a car by its ID.
- **Request Body**: None

### 4. Update a Car

- **URL**: `/cars/<uuid:car_id>/`
- **Method**: PATCH
- **Description**: Updates the details of a car by its ID.
- **Request Body Example**:

```json
{
  "colour": "Black",
  "mileage": 10000,
  "status": "m"
}
```

### 5. Delete a Car

- **URL**: `/cars/<uuid:car_id>/`
- **Method**: DELETE
- **Description**: Deletes a car by its ID. If the deleted car was the last one of its model or make, the model and make are also deleted.
- **Request Body**: None

### 6. Get Cars by Make

- **URL**: `/cars_by_make/<str:make_id>/`
- **Method**: GET
- **Description**: Retrieves all cars that belong to a specific make.
- **Request Body**: None

### 7. Get Cars by Model

- **URL**: `/get_cars_by_model/<str:model_id>/`
- **Method**: GET
- **Description**: Retrieves all cars that belong to a specific model.
- **Request Body**: None

### 8. Get All Makes

- **URL**: `/makes/`
- **Method**: GET
- **Description**: Retrieves a list of all car makes in the system.
- **Request Body**: None

### 9. Get All Car Models

- **URL**: `/models/`
- **Method**: GET
- **Description**: Retrieves a list of all car models in the system.
- **Request Body**: None

## Error Handling

- The API returns appropriate status codes and error messages in the response.
  - 404: If a car, make, or model is not found.
  - 400: If there is an issue with the input data (e.g., validation errors).
  - 405: If an unsupported HTTP method is used.

## Example API Responses

### GET /cars/

```json
[
  {
    "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "model": "Accord",
    "make": "Honda",
    "colour": "Red",
    "year": "2020",
    "VIN": "1HGCM82633A123456",
    "mileage": 15000,
    "status": "Available"
  },
  ...
]
```

### POST /cars/ (Create Car)

```json
{
  "car_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "make_created": false,
  "model_created": false,
  "message": "Car created successfully."
}
```

### GET /cars/<uuid:car_id>/

```json
{
  "id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
  "model": "Accord",
  "make": "Honda",
  "colour": "Red",
  "year": "2020",
  "VIN": "1HGCM82633A123456",
  "mileage": 15000,
  "status": "Available"
}
```

### PATCH /cars/<uuid:car_id>/

```json
{
  "car_model": "Accord",
  "car_make": "Honda",
  "colour": "Black",
  "year": "2022",
  "VIN": "1HGCM82633A123457",
  "mileage": 10000,
  "status": "Available"
}
```

### DELETE /cars/<uuid:car_id>/

```json
{
  "message": "Car deleted successfully"
}
```

## Setup and Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the migrations:
   ```bash
   python manage.py migrate
   ```
4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

## Authentication

This API does not currently require authentication, but it can be added using Django's authentication system or third-party packages such as Django Rest Framework.

## License

This project is licensed under the CC0 1.0 Universal License - see the LICENSE file for details.
