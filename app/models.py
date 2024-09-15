from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class Repartidor(Base):
    __tablename__ = "repartidores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    pedidos = relationship("PedidoEntregado", back_populates="repartidor")


class Producto(Base):
    __tablename__ = "productos"

    id = Column(String, primary_key=True, index=True)
    producto = Column(String, index=True)
    precio = Column(Float)


class PedidoEntregado(Base):
    __tablename__ = "pedidos_entregados"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(String, index=True)
    repartidor_id = Column(Integer, ForeignKey("repartidores.id"))
    timestamp = Column(DateTime)

    repartidor = relationship("Repartidor", back_populates="pedidos")
