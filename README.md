# API de Gestión de Coches y Conductores

**Autor**: Ignacio Martin Bravo

## Descripción General

API REST construida con **FastAPI** que gestiona el registro y control de conductores y vehículos asignados a ellos. El sistema permite crear, leer, actualizar y eliminar registros de conductores y sus coches asociados, manteniendo la relación entre ambas entidades.

---

## Temática Elegida

Se ha elegido un **sistema de gestión de conductores y vehículos** de una flota o empresa de transporte. Esta temática es realista y educativa porque:

- **Relación clara entre entidades**: cada vehículo (Coche) está asociado a un conductor específico
- **Casos de uso reales**: validación de duplicados, integridad referencial, operaciones CRUD completas
- **Validaciones prácticas**: verificación de conductores existentes, placas de matrícula únicas
- **Fácil de entender**: dominio cercano a la realidad cotidiana

---

## Entidades Creadas

### 1. **Conductor**
Representa a los conductores del sistema.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | Integer | Identificador único (clave primaria, autoincremental) |
| `nombre` | String | Nombre completo del conductor |
| `dni` | String | Documento Nacional de Identidad (único) |
| `genero` | String | Género del conductor |
| `telefono` | Integer | Número de teléfono de contacto |

**Endpoints**:
- `GET /conductor/` - Obtener todos los conductores
- `GET /conductor/{conductor_id}` - Obtener un conductor por ID
- `POST /conductor/` - Crear un nuevo conductor
- `PUT /conductor/{conductor_id}` - Actualizar un conductor
- `DELETE /conductor/{conductor_id}` - Eliminar un conductor

### 2. **Coche**
Representa los vehículos asignados a conductores.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | Integer | Identificador único (clave primaria, autoincremental) |
| `nombre` | String | Nombre o modelo del vehículo |
| `marca` | String | Marca del fabricante |
| `matricula` | String | Placa de matrícula (única) |
| `age` | Integer | Antigüedad o año del vehículo |
| `conductor_id` | Integer | ID del conductor (clave foránea) |

**Endpoints**:
- `GET /coche/` - Obtener todos los coches
- `GET /coche/{coche_id}` - Obtener un coche por ID
- `POST /coche/` - Crear un nuevo coche
- `PUT /coche/{coche_id}` - Actualizar un coche
- `DELETE /coche/{coche_id}` - Eliminar un coche

---

## Validaciones y Reglas de Negocio Implementadas

**Conductor**:
- El DNI debe ser único en el sistema
- No permite crear conductores duplicados

**Coche**:
- La matrícula debe ser única
- El conductor asignado debe existir en el sistema
- Valida la existencia del conductor antes de crear un coche

**Integridad Referencial**:
- No se permite asignar un coche a un conductor inexistente
- Manejo de errores con códigos HTTP apropiados (400, 404)

---

## Ampliaciones Opcionales Realizadas

### Características Adicionales

1. **Validación de Integridad Referencial**
   - Antes de crear un coche, se verifica que el conductor exista
   - Retorna error `404 (Not Found)` si el conductor no existe

2. **Códigos de Estado HTTP Adecuados**
   - `201 Created` - Al crear nuevos registros
   - `204 No Content` - Al eliminar registros
   - `400 Bad Request` - Para errores de validación (duplicados)
   - `404 Not Found` - Para recursos no encontrados

3. **Respuestas de Error Descriptivas**
   - Mensajes en español indicando el problema específico
   - Ejemplos: "El conductor ya existe", "Coche no encontrado"

4. **Arquitectura en Capas**
   - **Models**: Definición de entidades SQLAlchemy
   - **Schemas**: Modelos Pydantic para validación y serialización
   - **Routes**: Endpoints organizados por recurso
   - **Database**: Configuración de conexión y sesiones

---

## Configuración y Uso

### Crear y Activar Entorno Virtual (Windows PowerShell)

```powershell
python -m venv .venv
\.venv\Scripts\Activate.ps1
```

### Instalar Dependencias

```powershell
pip install -r requirements.txt
```

### Iniciar el Servidor FastAPI

```powershell
fastapi dev main.py
```

### Acceder a la Documentación

Abrir en el navegador: `http://127.0.0.1:8000/docs` (Swagger UI)

---

## Estructura del Proyecto

```
ApiPython/
├── main.py              # Punto de entrada de la aplicación
├── requirements.txt     # Dependencias del proyecto
├── test_api.rest        # Tests de la API
├── database/
│   ├── __init__.py
│   └── database.py      # Configuración de SQLAlchemy
├── models/
│   ├── __init__.py
│   ├── coche.py         # Modelo de Coche (SQLAlchemy ORM)
│   └── conductor.py     # Modelo de Conductor (SQLAlchemy ORM)
├── routes/
│   ├── __init__.py
│   ├── coche.py         # Endpoints de Coche
│   └── conductor.py     # Endpoints de Conductor
└── schemas/
    ├── coche.py         # Schemas Pydantic de Coche
    └── conductor.py     # Schemas Pydantic de Conductor
```

**Endpoints principales (resumen)**
- `GET /coches/` : lista coches
- `GET /coches/{id}` : obtiene un coche por id
- `POST /coches/` : crea un coche
- `PUT /coches/` : actualiza un coche
- `DELETE /coches/{id}` : elimina un coche
- `GET /propietarios/` y `GET /propietarios/{id}` : gestión de propietarios

Si quieres, puedo también añadir ejemplos de peticiones `curl` o un fichero `make` / scripts de lanzamiento para Windows.
