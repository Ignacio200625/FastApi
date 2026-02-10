from pydantic import BaseModel, EmailStr

class CocheBase(BaseModel):
    nombre:str
    marca:str
    matricula:str
    age:int
    conductor_id:int

class CocheCreate(CocheBase):
    pass

class CocheResponse(CocheBase):
    id: int

class Config:
    orm_mode = True