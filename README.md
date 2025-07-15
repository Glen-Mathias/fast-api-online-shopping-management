# FastAPI Online Shopping Order Management

A simple FastAPI-based backend for managing orders in an online shopping system. This project provides RESTful API endpoints for creating, reading, updating, and deleting (CRUD) orders, suitable for e-commerce platforms or as a learning resource for FastAPI.

## Features
- Create, list, update, and delete orders
- In-memory data storage (easy to extend to a real database)
- Automatic OpenAPI docs via Swagger UI
- Type-safe models using Pydantic

## Tech Stack
- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Glen-Mathias/fast-api-online-shopping-management.git
   cd fast-api-online-shopping-management
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

### Running the Application
Start the development server with:
```bash
uvicorn main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API documentation (Swagger UI).

## API Endpoints

### Health Check
- `GET /`
  - **Response:** `{ "message": "Order Management API is running" }`

### Orders
- `POST /orders`
  - **Description:** Create a new order
  - **Request Body:**
    ```json
    {
      "customer_name": "John Doe",
      "items": [
        { "product_id": 1, "quantity": 2 },
        { "product_id": 2, "quantity": 1 }
      ]
    }
    ```
  - **Response:** Order object with `id`

- `GET /orders`
  - **Description:** List all orders
  - **Response:** Array of order objects

- `GET /orders/{order_id}`
  - **Description:** Get a specific order by ID
  - **Response:** Order object

- `PUT /orders/{order_id}`
  - **Description:** Update an existing order
  - **Request Body:** Same as POST /orders
  - **Response:** Updated order object

- `DELETE /orders/{order_id}`
  - **Description:** Delete an order by ID
  - **Response:** `{ "message": "Order {order_id} deleted successfully" }`

## Example Order Object
```json
{
  "id": 1,
  "customer_name": "John Doe",
  "items": [
    { "product_id": 1, "quantity": 2 },
    { "product_id": 2, "quantity": 1 }
  ]
}
```

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

## License
This project is licensed under the MIT License.
