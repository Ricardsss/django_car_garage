# Car Garage API

This is the API documentation for the Django project, which includes user authentication (registration, login, and logout) and managing cars, makes, and models.

## Endpoints

## Authentication

### Register a New User

**Endpoint:** `POST /accounts/register/`

**Request Body:**

```json
{
  "username": "john",
  "email": "lennon@thebeatles.com",
  "password": "johnpassword",
  "first_name": "John",
  "last_name": "Lennon"
}
```

**Response:**

```json
{
  "message": "User registered successfully.",
  "user": {
    "id": 1,
    "username": "john",
    "email": "lennon@thebeatles.com",
    "first_name": "John",
    "last_name": "Lennon"
  }
}
```

### Login

**Endpoint:** `POST /accounts/login/`

**Request Body:**

```json
{
  "username": "john",
  "password": "johnpassword"
}
```

**Response:**

```json
{
  "message": "Login successful"
}
```

### Logout

**Endpoint:** `DELETE /accounts/logout/`

**Request:**

No body required.

**Response:**

```json
{
  "message": "You have successfully logged out."
}
```

## Cars Management

### Get All Cars

**Endpoint:** `GET /garage/cars/`

**Response:**

```json
[
  {
    "id": "1",
    "model": "Civic",
    "make": "Honda",
    "colour": "Red",
    "year": "2020",
    "VIN": "1HGCM82633A123456",
    "mileage": 5000,
    "status": "Available"
  },
  {
    "id": "2",
    "model": "Model S",
    "make": "Tesla",
    "colour": "Black",
    "year": "2021",
    "VIN": "5YJSA1E23MF123456",
    "mileage": 1000,
    "status": "Rented"
  }
]
```

### Get a Specific Car

**Endpoint:** `GET /garage/cars/{car_id}/`

**Response:**

```json
{
  "id": "1",
  "model": "Civic",
  "make": "Honda",
  "colour": "Red",
  "year": "2020",
  "VIN": "1HGCM82633A123456",
  "mileage": 5000,
  "status": "Available"
}
```

### Create a Car

**Endpoint:** `POST /garage/cars/`

**Request Body:**

```json
{
  "make_name": "Honda",
  "model_name": "Civic",
  "colour": "Red",
  "year": "2020",
  "VIN": "1HGCM82633A123456",
  "mileage": 5000
}
```

**Response:**

```json
{
  "car_id": 1,
  "make_created": false,
  "model_created": false,
  "message": "Car created successfully."
}
```

### Update a Car

**Endpoint:** `PATCH /garage/cars/{car_id}/`

**Request Body:**

```json
{
  "colour": "Blue",
  "mileage": 6000
}
```

**Response:**

```json
{
  "id": "1",
  "model": "Civic",
  "make": "Honda",
  "colour": "Blue",
  "year": "2020",
  "VIN": "1HGCM82633A123456",
  "mileage": 6000,
  "status": "Available"
}
```

### Delete a Car

**Endpoint:** `DELETE /garage/cars/{car_id}/`

**Response:**

```json
{
  "message": "Car deleted successfully"
}
```

## Make and Model Management

### Get All Makes

**Endpoint:** `GET /garage/makes/`

**Response:**

```json
[
  {
    "id": 1,
    "name": "Honda"
  },
  {
    "id": 2,
    "name": "Tesla"
  }
]
```

### Get All Models

**Endpoint:** `GET /garage/models/`

**Response:**

```json
[
  {
    "id": 1,
    "name": "Civic",
    "make": "Honda"
  },
  {
    "id": 2,
    "name": "Model S",
    "make": "Tesla"
  }
]
```

### Get Cars by Make

**Endpoint:** `GET /garage/cars_by_make/{make_id}/`

**Response:**

```json
[
  {
    "id": "1",
    "model": "Civic",
    "make": "Honda",
    "colour": "Red",
    "year": "2020",
    "VIN": "1HGCM82633A123456",
    "mileage": 5000,
    "status": "Available"
  }
]
```

### Get Cars by Model

**Endpoint:** `GET /garage/cars_by_model/{model_id}/`

**Response:**

```json
[
  {
    "id": "1",
    "model": "Civic",
    "make": "Honda",
    "colour": "Red",
    "year": "2020",
    "VIN": "1HGCM82633A123456",
    "mileage": 5000,
    "status": "Available"
  }
]
```

## Setup and Installation

1. Clone the repository.
2. Change into the project folder
   ```bash
   cd cargarage
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

## License

This project is licensed under the CC0 1.0 Universal License - see the LICENSE file for details.
