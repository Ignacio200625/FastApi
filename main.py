from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()


class Conductor(BaseModel):
    id:int
    
propietarios=[
    Conductor(id=1),
    Conductor(id=2),
    Conductor(id=3)
]    

def get_propietario(id: int):
    for p in propietarios:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Propietario no encontrado")
    
class Coche(BaseModel):
    id:int
    nombre:str
    marca:str
    combustible:str
    antiguedad:int
    propietario:Conductor
    
coches=[
    Coche(id=1,
        nombre="Mustang",
        marca="Ford",
        combustible="Diesel",
        antiguedad=20,
        propietario=get_propietario(2)
    ),Coche(
        id=2,
        nombre="Veyron",
        marca="Bugatti",
        combustible="Gasolina",
        antiguedad=10,
        propietario=get_propietario(1)
    )
    ,Coche(
        id=3,
        nombre="M4",
        marca="BMW",
        combustible="Diesel",
        antiguedad=5,
        propietario=get_propietario(3)
    )
]

@app.get("/coches/",tags=["Coches"])
async def get_coches():
    return coches
    

    
@app.get("/coches/{id}",responses={
        404: {
            "description": "Item no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Item no encontrado"}
                }
            }
        }
    },response_model=Coche,tags=["Coches"])
async def get_coche_by_id(id: int):
    return search_coche(id)

def search_coche(id:int):
    coches_filtered = filter(lambda  user:user.id == id , coches)
    try:
        return list(coches_filtered)[0]
    except:
        raise HTTPException(status_code=404,detail="Coche no encontrado")
    

@app.post("/coches/",response_model=Coche,responses={
        409: {
            "description": "Este ID ya esta en uso",
            "content": {
                "application/json": {
                    "example": {"detail": "Este ID ya esta en uso"}
                }
            }
        }
    },status_code=201,tags=["Coches"])
async def  add_coche(coche:Coche):
    
    search_propietario(coche.propietario.id)
    
    if any(coche_stored.id == coche.id for coche_stored in coches):
        raise HTTPException(status_code=409,detail="Ese ID ya esta en uso")
    else:
        coches.append(coche)
        return coche



def get_propietario(id: int):
    for p in propietarios:
        if p.id == id:
            return p
    raise HTTPException(status_code=404, detail="Propietario no encontrado")

@app.get("/coches/{id}/propietario", response_model=Conductor,tags=["Coches"])
async def get_propietario_by_coche(id: int):
    # busca el coche
    for c in coches:
        if c.id == id:
            return c.propietario

    raise HTTPException(status_code=404, detail="Coche no encontrado")

@app.put("/coches/",response_model=Coche,tags=["Coches"])
async def put_user(coche:Coche):
    found = False
    for index ,saved_coche in enumerate(coches):
        if saved_coche.id ==coche.id:
            coches[index] = coche
            found=True
    
    if not found:
        raise HTTPException(status_code=404,detail="Usuario no encontrado")
    else:
        return coche

@app.delete("/coches/{id}",tags=["Coches"])
async def delete_coche(id:int):
    found = False
    for index ,saved_coche in enumerate(coches):
        if saved_coche.id ==id:
            del coches[index]
            found=True
    
    if not found:
        raise HTTPException(status_code=404,detail="Coche no encontrado")
    else:
        return  {"message":"Coche Eliminado"}

@app.get("/propietarios/",tags=["Propietarios"])
async def get_propietarios():
    return propietarios

@app.get("/propietarios/{id}",responses={
        404: {
            "description": "Item no encontrado",
            "content": {
                "application/json": {
                    "example": {"detail": "Item no encontrado"}
                }
            }
        }
    },response_model=Conductor,tags=["Propietarios"])
async def get_propietario_by_id(id: int):
    return search_propietario(id)

def search_propietario(id:int):
    propietarios_filtered = filter(lambda  user:user.id == id , propietarios)
    try:
        return list(propietarios_filtered)[0]
    except:
        raise HTTPException(status_code=404,detail="Propietario no encontrado")
    

@app.post("/propietarios/",response_model=Conductor,responses={
        409: {
            "description": "Este ID ya esta en uso",
            "content": {
                "application/json": {
                    "example": {"detail": "Este ID ya esta en uso"}
                }
            }
        }
    },status_code=201,tags=["Propietarios"])
async def  add_propietario(propietario:Conductor):
    
    if any(propietario_stored.id == propietario.id for propietario_stored in propietarios):
        raise HTTPException(status_code=409,detail="Ese ID ya esta en uso")
    else:
        propietarios.append(propietario)
        return propietario


@app.delete("/propietarios/{id}",tags=["Propietarios"])
async def delete_propietario(id:int):
    found = False
    for index ,propietarios_coche in enumerate(propietarios):
        if propietarios_coche.id ==id:
            del propietarios[index]
            found=True

    if not found:
        raise HTTPException(status_code=404,detail="Propietario no encontrado")
    else:
        return  {"message":"Propietario Eliminado"}
    
    
