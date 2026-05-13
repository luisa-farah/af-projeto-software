from fastapi import FastAPI
from app.database import Base, engine
from app.routers import imoveis

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Imóveis")

app.include_router(imoveis.router)