from pydantic import BaseModel
from typing import List, Optional

class OrderItem(BaseModel):
    """Represents an item in an order."""
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    """Schema for creating a new order."""
    customer_name: str
    items: List[OrderItem]

class Order(OrderCreate):
    """Order model with unique identifier."""
    id: int
