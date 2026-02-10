from fastapi import FastAPI

from database.database import Base, engine
from routes import coche,conductor
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:3000"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

app.include_router(coche.router)

app.include_router(conductor.router)

@app.get("/")
def root():
    return {"message": "API de usuarios con FastAPI y SQLite"}