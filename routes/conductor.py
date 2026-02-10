from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database.database import SessionLocal
from models.conductor import Conductor
from schemas.conductor import ConductorCreate, ConductorResponse

router = APIRouter(
    prefix="/conductor",
    tags=["conductores"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[ConductorResponse])
def get_conductores(db: Session = Depends(get_db)):
    return db.query(Conductor).all()

@router.get("/{conductor_id}", response_model=ConductorResponse)
def get_conductor(conductor_id: int, db: Session = Depends(get_db)):
    conductor = db.query(Conductor).filter(Conductor.id == conductor_id).first()
    if not conductor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conductor no encontrado"
        )
    return conductor

@router.post("/", response_model=ConductorResponse, status_code=status.HTTP_201_CREATED)
def create_conductor(conductor: ConductorCreate, db: Session = Depends(get_db)):
    existing_conductor = db.query(Conductor).filter(
        Conductor.dni == conductor.dni
    ).first()

    if existing_conductor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El conductor ya existe"
        )

    new_conductor = Conductor(**conductor.dict())
    db.add(new_conductor)
    db.commit()
    db.refresh(new_conductor)
    return new_conductor

@router.put("/{conductor_id}", response_model=ConductorResponse)
def update_conductor(conductor_id: int, conductor: ConductorCreate, db: Session = Depends(get_db)):
    stored_conductor = db.query(Conductor).filter(Conductor.id == conductor_id).first()

    if not stored_conductor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conductor no encontrado"
        )

    for key, value in conductor.model_dump().items():
        setattr(stored_conductor, key, value)

    db.commit()
    db.refresh(stored_conductor)
    return stored_conductor

@router.delete("/{conductor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_conductor(conductor_id: int, db: Session = Depends(get_db)):
    conductor = db.query(Conductor).filter(Conductor.id == conductor_id).first()

    if not conductor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conductor no encontrado"
        )

    db.delete(conductor)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
