# API DE COCHES Y PROPIETARIOS 

**Nombre**: Ignacio Martin Bravo

**Resumen**
- **Proyecto**: API REST simple construida con FastAPI que gestiona coches y propietarios.


- **Crear y activar un entorno virtual (`.venv`) (recomendado)**: en Windows PowerShell desde la carpeta del proyecto:
  
```powershell
python -m venv .venv
\.venv\Scripts\Activate.ps1
```

**Cómo lanzar el servidor FastAPI**
- **Instalar dependencias**: ejecutar desde la raíz del proyecto:

```powershell
pip install -r requirements.txt
```



- **Nota**: en este proyecto instalamos también `fastapi` (y `fastapi-cli` si desea usar la CLI). Al usar el entorno virtual, las instalaciones con `pip` quedan aisladas del Python global. Si prefiere instalar `fastapi` manualmente puede ejecutar:

```powershell
pip install fastapi 
```


- **Iniciar servidor (PowerShell)**: estando en la carpeta `c:\ApiPython` ejecutar:



```powershell
fastapi dev main.py
```

	- Nota: el comando `fastapi dev main.py` es proporcionado por la utilidad `fastapi-cli` (el proyecto incluye `fastapi-cli` en `requirements.txt`). Este comando lanza el servidor de desarrollo por debajo usando `uvicorn` (con recarga automática), por eso el resultado es equivalente al comando `uvicorn main:app --reload ...`.

- **Acceder a la API**: abrir `http://127.0.0.1:8000/docs` en el navegador para la documentación automática (Swagger UI).

**Justificación del dominio de datos elegido**
- **Dominio**: coches y propietarios (modelos `Coche` y `Conductor` / `Propietario`).
- **Por qué**: este dominio es sencillo y cercano al mundo real, por lo que es ideal para enseñar y probar conceptos esenciales de APIs REST:
	- **Relaciones anidadas**: cada `Coche` tiene un `propietario` embebido, lo que permite demostrar modelos anidados y validación con Pydantic.
	- **Operaciones CRUD completas**: permite implementar y probar crear, leer, actualizar y borrar tanto coches como propietarios.
	- **Campos representativos**: campos como `marca`, `combustible` y `antiguedad` son realistas y suficientes para cubrir validaciones y filtros básicos sin añadir complejidad innecesaria.
	- **Clara separación de responsabilidades**: facilita probar rutas, respuestas de error (404, 409) y ejemplos de respuesta.

**Endpoints principales (resumen)**
- `GET /coches/` : lista coches
- `GET /coches/{id}` : obtiene un coche por id
- `POST /coches/` : crea un coche
- `PUT /coches/` : actualiza un coche
- `DELETE /coches/{id}` : elimina un coche
- `GET /propietarios/` y `GET /propietarios/{id}` : gestión de propietarios

Si quieres, puedo también añadir ejemplos de peticiones `curl` o un fichero `make` / scripts de lanzamiento para Windows.
