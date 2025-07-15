from fastapi import FastAPI, HTTPException
from typing import List
from models import Order, OrderCreate, OrderItem

app = FastAPI(title="Order Management API")

# Simulated in-memory database for demonstration purposes
orders_db: List[Order] = []
next_order_id: int = 1

def get_order_by_id(order_id: int) -> Order:
    """Helper function to retrieve an order by its ID."""
    for order in orders_db:
        if order.id == order_id:
            return order
    return None

@app.get("/", tags=["Health"])
def root() -> dict:
    """Health check endpoint."""
    return {"message": "Order Management API is running"}

@app.post("/orders", response_model=Order, tags=["Orders"])
def create_order(order: OrderCreate) -> Order:
    """Create a new order."""
    global next_order_id
    new_order = Order(id=next_order_id, **order.dict())
    orders_db.append(new_order)
    next_order_id += 1
    return new_order

@app.get("/orders", response_model=List[Order], tags=["Orders"])
def list_orders() -> List[Order]:
    """List all orders."""
    return orders_db

@app.get("/orders/{order_id}", response_model=Order, tags=["Orders"])
def get_order(order_id: int) -> Order:
    """Retrieve a specific order by ID."""
    order = get_order_by_id(order_id)
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.put("/orders/{order_id}", response_model=Order, tags=["Orders"])
def update_order(order_id: int, updated_order: OrderCreate) -> Order:
    """Update an existing order by ID."""
    for idx, order in enumerate(orders_db):
        if order.id == order_id:
            new_order = Order(id=order_id, **updated_order.dict())
            orders_db[idx] = new_order
            return new_order
    raise HTTPException(status_code=404, detail="Order not found")

@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_order(order_id: int) -> dict:
    """Delete an order by ID."""
    for idx, order in enumerate(orders_db):
        if order.id == order_id:
            del orders_db[idx]
            return {"message": f"Order {order_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Order not found")

