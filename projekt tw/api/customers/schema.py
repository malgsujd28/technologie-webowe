from pydantic import BaseModel

class CustomerCreateSchema(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski",
                "email": "jan.kowalski@example.com",
                "phone_number": "000-000-000",
            }
        }


class CustomerUpdateSchema(BaseModel):
    name: str | None
    surname: str | None
    email: str | None
    phone_number: str | None

    class Config:
        schema_extra = {
            "example": {
                "name": "Jan",
                "surname": "Kowalski"
            }
        }


class Customer(CustomerCreateSchema):
    id: int

class ProductCreateSchema(BaseModel):
    price: float
    name: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "price": 27.0,
                "name": "mug",
                "description": "mug with capibara",
            }
        }

class Product(ProductCreateSchema):
    id:int

class OrderCreateSchema(BaseModel):
    customer_id: int
    products_id: list[int]

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 0,
                "products_id": [0, 1]
            }
        }

class Order(OrderCreateSchema):
    id:int