from fastapi import APIRouter, HTTPException, Query

from .storage import get_customers_storage, get_products_storage, get_orders_storage
from .schema import CustomerCreateSchema, CustomerUpdateSchema, Customer, ProductCreateSchema, Product, OrderCreateSchema, Order

router = APIRouter()


CUSTOMERS_STORAGE = get_customers_storage()
PRODUCTS_STORAGE = get_products_storage()
ORDERS_STORAGE = get_orders_storage()

@router.get("/customers")
async def get_customers() -> list[Customer]:
    return list(get_customers_storage().values())


@router.get("/customers/{customer_id}")
async def get_customer(customer_id: int) -> Customer:
    try:
        return CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )


@router.patch("/customers/{customer_id}")
async def update_customer(
    customer_id: int, updated_customer: CustomerUpdateSchema
) -> Customer:
    existing_customer = None
    try:
       existing_customer = CUSTOMERS_STORAGE[customer_id]
    except KeyError:
       raise HTTPException(
           status_code=404, detail=f"There is no customer with id {customer_id}"
       )
    if updated_customer.name:
        existing_customer.name = updated_customer.name
    if updated_customer.surname:
        existing_customer.surname = updated_customer.surname
    if updated_customer.email:
        existing_customer.email = updated_customer.email
    if updated_customer.phone_number:
        existing_customer.phone_number = updated_customer.phone_number
    return existing_customer


@router.delete("/customers/{customer_id}")
async def delete_customer(customer_id: int) -> None:
    try:
        del CUSTOMERS_STORAGE[customer_id]
    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Customer with ID={customer_id} does not exist."
        )

@router.post("/customers")
async def create_customer(customer: CustomerCreateSchema) -> Customer:
   index = len(CUSTOMERS_STORAGE)
   CUSTOMERS_STORAGE[index] = Customer(id=index, name=customer.name, surname=customer.surname, email=customer.email, phone_number=customer.phone_number)
   return CUSTOMERS_STORAGE[index]

@router.get("/products")
async def get_products() -> list[Product]:
    return list(get_products_storage().values())

@router.post("/products")
async def create_product(product: ProductCreateSchema) -> Product:
   index = len(PRODUCTS_STORAGE)
   PRODUCTS_STORAGE[index] = Product(id=index, price=product.price, name=product.name, description=product.description)
   return PRODUCTS_STORAGE[index]

@router.get("/orders")
async def get_orders() -> list[Order]:
    return list(get_orders_storage().values())

@router.post("/orders")
async def create_order(order: OrderCreateSchema) -> Order:
   index = len(ORDERS_STORAGE)
   ORDERS_STORAGE[index] = Order(id=index, customer_id=order.customer_id , products_id=order.products_id)
   return ORDERS_STORAGE[index]
