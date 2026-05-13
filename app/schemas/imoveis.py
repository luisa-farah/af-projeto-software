from pydantic import BaseModel, EmailStr
from datetime import datetime
from decimal import Decimal

from app.models.imovel import StatusImovel


class ImovelCreate(BaseModel):
    codigo_imovel: str
    preco: Decimal
    status: StatusImovel
    email_admin: EmailStr


class ImovelResponse(ImovelCreate):
    id: int
    data_cadastro: datetime

    model_config = {"from_attributes": True}
