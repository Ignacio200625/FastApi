from pydantic import BaseModel

class ConductorBase(BaseModel):
    nombre: str
    dni: str
    genero: str
    telefono: int
    
    
class ConductorCreate(ConductorBase):
    pass

class ConductorResponse(ConductorBase):
    id: int

class Config:
    orm_mode = True