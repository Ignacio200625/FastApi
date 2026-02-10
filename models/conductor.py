from sqlalchemy import Column, Integer, String
from database.database import Base
    
class Conductor(Base):
    __tablename__="conductor"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    dni = Column(String, nullable=False)
    telefono = Column(Integer, nullable=False)      