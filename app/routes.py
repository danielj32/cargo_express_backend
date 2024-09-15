from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models import PedidoEntregado, Repartidor,Producto
from datetime import datetime, timedelta

router = APIRouter()

# Modelo para recibir los datos del pedido entregado
class PedidoInput(BaseModel):
    pedido_id: str
    repartidor: dict
    productos: list
    timestamp: str

# Ruta para registrar un pedido entregado
@router.post("/registrar_pedido_entregado/")
def registrar_pedido(pedido: PedidoInput, db: Session = Depends(get_db)):
    # Validar si el repartidor existe
    repartidor = db.query(Repartidor).filter_by(IdRepartidor=pedido.repartidor["IdRepartidor"]).first()
    if not repartidor:
        raise HTTPException(status_code=404, detail="Repartidor no encontrado")
    
    # Procesar cada producto del pedido
    for prod in pedido.productos:
        producto = db.query(Producto).filter_by(IdProducto=prod["IdProducto"]).first()
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto {prod['producto']} no encontrado")
        
        # Registrar el pedido en la base de datos
        nuevo_pedido = PedidoEntregado(
            id=pedido.pedido_id,
            repartidor_id=repartidor.IdRepartidor,
            producto_id=producto.IdProducto,
            timestamp=pedido.timestamp
        )
        db.add(nuevo_pedido)
    
    db.commit()
    return {"message": "Pedido registrado exitosamente"}

# Ruta para calcular las entregas por hora de un repartidor
@router.get("/entregas_por_hora/")
def entregas_por_hora(repartidor_id: int, db: Session = Depends(get_db)):
    # Obtener el tiempo actual y calcular el inicio de la hora anterior
    tiempo_actual = datetime.now()
    inicio_hora = tiempo_actual - timedelta(hours=1)
    
    # Obtener el número de pedidos entregados por el repartidor en la última hora
    entregas = db.query(PedidoEntregado).filter(
        PedidoEntregado.repartidor_id == repartidor_id,
        PedidoEntregado.timestamp >= inicio_hora,
        PedidoEntregado.timestamp <= tiempo_actual
    ).count()
    
    # Si no hay entregas, devolver un mensaje adecuado
    if entregas == 0:
        return {"message": f"El repartidor con ID {repartidor_id} no ha realizado entregas en la última hora."}
    
    return {"repartidor_id": repartidor_id, "entregas_ultima_hora": entregas}
