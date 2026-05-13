from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import Base, engine, get_db
from app.schemas.imovel import ImovelCreate, ImovelResponse
from app import imovel as crud
from app.models.imovel import Imovel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Imóveis")


@app.get("/properties", response_model=List[ImovelResponse])
def listar(db: Session = Depends(get_db)):
    return crud.get_all(db)


@app.post("/properties", response_model=ImovelResponse, status_code=201)
def criar(data: ImovelCreate, db: Session = Depends(get_db)):
    return crud.create(db, data)


@app.delete("/properties/{imovel_id}", response_model=ImovelResponse)
def deletar(imovel_id: int, db: Session = Depends(get_db)):
    imovel = crud.delete(db, imovel_id)
    if not imovel:
        raise HTTPException(status_code=404, detail="Imóvel não encontrado")
    return imovel