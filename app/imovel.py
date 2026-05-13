from sqlalchemy.orm import Session
from app.models.imovel import Imovel
from app.schemas.imovel import ImovelCreate, ImovelUpdate


def get_all(db: Session):
    return db.query(Imovel).all()


def get_by_id(db: Session, imovel_id: int):
    return db.query(Imovel).filter(Imovel.id == imovel_id).first()


def create(db: Session, data: ImovelCreate):
    imovel = Imovel(**data.model_dump())
    db.add(imovel)
    db.commit()
    db.refresh(imovel)
    return imovel


def update(db: Session, imovel_id: int, data: ImovelUpdate):
    imovel = get_by_id(db, imovel_id)
    if not imovel:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(imovel, field, value)
    db.commit()
    db.refresh(imovel)
    return imovel


def delete(db: Session, imovel_id: int):
    imovel = get_by_id(db, imovel_id)
    if not imovel:
        return None
    db.delete(imovel)
    db.commit()
    return imovel
