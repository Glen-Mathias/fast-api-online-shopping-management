# FastAPI Online Shopping Order Management API

A FastAPI-based RESTful backend for managing customer orders in an online shopping system. The application provides CRUD operations for orders and includes interactive API documentation using Swagger UI.

## 🚀 Live Demo

- **Live API:** https://fast-api-online-shopping-management-api.onrender.com/
- **Swagger Documentation:** https://fast-api-online-shopping-management-api.onrender.com/docs
- **ReDoc Documentation:** https://fast-api-online-shopping-management-api.onrender.com/redoc

## Features

- Create new customer orders
- Retrieve all orders
- Retrieve an order by ID
- Update existing orders
- Delete orders
- Automatic interactive API documentation (Swagger UI)
- Type-safe request and response validation using Pydantic
- Built with FastAPI

## Tech Stack

- Python 3.7+
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```
fast-api-online-shopping-management/
│
├── main.py
├── models.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository

```bash
git clone https://github.com/Glen-Mathias/fast-api-online-shopping-management.git
cd fast-api-online-shopping-management
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server

```bash
uvicorn main:app --reload
```

The application will be available at:

- Local API: http://127.0.0.1:8000/
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

# Live Deployment

The project is deployed on Render.

### Base URL

```
https://fast-api-online-shopping-management-api.onrender.com
```

### Interactive Swagger Documentation

```
https://fast-api-online-shopping-management-api.onrender.com/docs
```

Recruiters and users can test all endpoints directly from the Swagger interface without installing the project locally.

---

# API Endpoints

## Health Check

### GET /

Returns the application status.

Example Response

```json
{
  "message": "Order Management API is running"
}
```

---

## Orders

### POST /orders

Create a new order.

Example Request

```json
{
  "customer_name": "John Doe",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 2,
      "quantity": 1
    }
  ]
}
```

---

### GET /orders

Returns all orders.

---

### GET /orders/{order_id}

Returns a specific order by its ID.

---

### PUT /orders/{order_id}

Updates an existing order.

---

### DELETE /orders/{order_id}

Deletes an order.

Example Response

```json
{
  "message": "Order 1 deleted successfully"
}
```

---

## Example Order Object

```json
{
  "id": 1,
  "customer_name": "John Doe",
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 2,
      "quantity": 1
    }
  ]
}
```

## Future Improvements

- MongoDB Atlas integration
- Authentication & Authorization (JWT)
- Order status tracking
- Product inventory management
- Docker support
- CI/CD pipeline using GitHub Actions

## License

This project is licensed under the MIT License.
