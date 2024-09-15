from pydantic import BaseModel
from typing import List

class ProductoSchema(BaseModel):
    IdProducto: str
    Producto: str
    Precio: float

class PedidoEntregadoSchema(BaseModel):
    pedido_id: str
    repartidor_id: int
    productos: List[ProductoSchema]
