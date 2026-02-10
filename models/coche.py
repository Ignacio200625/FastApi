from sqlalchemy import ForeignKey, Column, Integer, String
from database.database import Base
    
class Coche(Base):
    __tablename__="coche"
        
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    matricula = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    conductor_id = Column(Integer, ForeignKey("conductor.id"), nullable=False)    
   