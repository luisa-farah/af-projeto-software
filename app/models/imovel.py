from sqlalchemy import Column, Integer, String, Numeric, DateTime, Enum
from sqlalchemy.sql import func
import enum

from app.database import Base


class StatusImovel(str, enum.Enum):
    disponivel = "disponivel"
    vendido = "vendido"
    cancelado = "cancelado"


class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True, index=True)
    codigo_imovel = Column(String, unique=True, nullable=False, index=True)
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    preco = Column(Numeric(12, 2), nullable=False)
    status = Column(Enum(StatusImovel), nullable=False, default=StatusImovel.disponivel)
    email_admin = Column(String, nullable=False)
