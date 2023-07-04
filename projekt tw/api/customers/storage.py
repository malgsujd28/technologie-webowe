from functools import lru_cache

from .schema import Customer, Product, Order


CustomerStorageType = dict[int, Customer]
ProductStorage = dict[int, Product]
OrderStorage = dict[int, Order]

CUSTOMERS: CustomerStorageType = {}
PRODUCTS: ProductStorage = {}
ORDERS: OrderStorage = {}


@lru_cache(maxsize=1)
def get_customers_storage() -> CustomerStorageType:
    return CUSTOMERS

@lru_cache(maxsize=1)
def get_products_storage() -> ProductStorage:
    return PRODUCTS

@lru_cache(maxsize=1)
def get_orders_storage() -> OrderStorage:
    return ORDERS