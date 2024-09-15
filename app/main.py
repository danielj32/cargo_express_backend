from fastapi import FastAPI
from app.database import engine, Base
from app.routes import router as pedido_router
from app.models import Repartidor, Producto, PedidoEntregado  # Importar desde models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Cargo Express!"}

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.include_router(pedido_router)
