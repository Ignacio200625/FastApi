from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from database.database import SessionLocal
from models.coche import Coche
from models.conductor import Conductor  
from schemas.coche import CocheCreate, CocheResponse

router = APIRouter(
    prefix="/coche",
    tags=["coches"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CocheResponse])
def get_coches(db: Session = Depends(get_db)):
    return db.query(Coche).all()

@router.get("/{coche_id}", response_model=CocheResponse)
def get_coche(coche_id: int, db: Session = Depends(get_db)):
    coche = db.query(Coche).filter(Coche.id == coche_id).first()
    if not coche:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coche no encontrado"
        )
    return coche

@router.post("/", response_model=CocheResponse, status_code=status.HTTP_201_CREATED)
def create_coche(coche: CocheCreate, db: Session = Depends(get_db)):
    # Comprobamos que el coche no exista
    existing_coche = db.query(Coche).filter(
        Coche.matricula == coche.matricula
    ).first()
    if existing_coche:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El coche ya existe"
        )
    
    # Comprobamos que el conductor exista
    conductor = db.query(Conductor).filter(Conductor.id == coche.conductor_id).first()
    if not conductor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conductor no encontrado"
        )

    new_coche = Coche(**coche.dict())
    db.add(new_coche)
    db.commit()
    db.refresh(new_coche)
    return new_coche

@router.put("/{coche_id}", response_model=CocheResponse)
def update_coche(coche_id: int, coche: CocheCreate, db: Session = Depends(get_db)):
    stored_coche = db.query(Coche).filter(Coche.id == coche_id).first()
    if not stored_coche:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coche no encontrado"
        )

    for key, value in coche.dict().items():
        setattr(stored_coche, key, value)

    db.commit()
    db.refresh(stored_coche)
    return stored_coche

@router.delete("/{coche_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_coche(coche_id: int, db: Session = Depends(get_db)):
    coche = db.query(Coche).filter(Coche.id == coche_id).first()
    if not coche:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Coche no encontrado"
        )

    db.delete(coche)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
