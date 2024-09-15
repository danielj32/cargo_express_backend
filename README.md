Cargo Express Backend
Este proyecto es el backend para la aplicación de gestión de pedidos de la empresa de mensajería Cargo Express. Utiliza FastAPI para el desarrollo de la API y SQLite para el almacenamiento de datos.

Tabla de Contenidos
Descripción
Requisitos
Instalación
Configuración
Uso
Pruebas
Diagrama de Arquitectura
Contribución
Licencia
Descripción
La aplicación permite registrar entregas de productos en tiempo real y monitorear métricas relacionadas con los repartidores y los productos. Incluye las siguientes funcionalidades:

Registrar Pedidos Entregados: Permite registrar los detalles de los pedidos entregados por los repartidores.
Entregas por Hora: Calcula la cantidad de entregas realizadas por un repartidor en la última hora.
Productos Más Vendidos: Obtiene los productos más vendidos en la última hora.
Requisitos
Python 3.12
FastAPI
SQLAlchemy
SQLite
Instalación
Clona el repositorio:

bash
Copiar código
git clone https://github.com/tu_usuario/cargo_express_backend.git
cd cargo_express_backend
Crea un entorno virtual:

bash
Copiar código
python -m venv venv
Activa el entorno virtual:

En Windows:

bash
Copiar código
venv\Scripts\activate
En macOS/Linux:

bash
Copiar código
source venv/bin/activate
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Aplica las migraciones a la base de datos:

bash
Copiar código
python -m app.main
Configuración
Archivo de Configuración: Asegúrate de que el archivo database.py tenga configurada la URL correcta de la base de datos (actualmente configurado para SQLite local).
Uso
Para iniciar la aplicación, ejecuta el siguiente comando:

bash
Copiar código
uvicorn app.main:app --reload
Esto iniciará el servidor en http://127.0.0.1:8000. Puedes acceder a la documentación interactiva de la API en http://127.0.0.1:8000/docs o en http://127.0.0.1:8000/redoc.

Pruebas
Para probar la aplicación, puedes utilizar herramientas como curl, Postman o simplemente interactuar con la documentación interactiva proporcionada por FastAPI.

Registrar Pedido Entregado
Método: POST

Endpoint: /registrar_pedido_entregado/

Cuerpo de la Solicitud:

json
Copiar código
{
    "pedido_id": "string",
    "repartidor": {
        "IdRepartidor": 101
    },
    "productos": [
        {
            "IdProducto": "pk0001",
            "producto": "Moneda",
            "precio": 1.00
        }
    ],
    "timestamp": "2024-09-14T12:00:00"
}
Consultar Entregas por Hora
Método: GET

Endpoint: /entregas_por_hora/

Parámetro: repartidor_id (int)

Ejemplo:

bash
Copiar código
curl "http://127.0.0.1:8000/entregas_por_hora/?repartidor_id=101"
Diagrama de Arquitectura
A continuación se presenta un diagrama básico de la arquitectura de la aplicación:

plaintext
Copiar código
+----------------+          +----------------+          +----------------+
|   Cliente API  |  <--->   |     FastAPI    |  <--->   |    SQLite DB   |
|                |          |    (Backend)   |          |                |
| - Postman      |          |                |          |                |
| - cURL          |         |                |          |                |
+----------------+          +----------------+          +----------------+
Cliente API: Herramientas como Postman o cURL utilizadas para interactuar con la API.
FastAPI: El backend que maneja las solicitudes HTTP, la lógica de negocio y la comunicación con la base de datos.
SQLite DB: Base de datos local que almacena los datos de los pedidos, productos y repartidores.
