from fastapi import FastAPI
from api.v1.api import api_router
from database import Base, engine


app = FastAPI(title="Hackathon SantoDigital 2024")

Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix="/api/v1")
