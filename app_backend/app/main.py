from fastapi import FastAPI
from app.api.routes.documents import router as document_router
from app.api.routes.vessels import router as vessel_router
from app.database import Base, engine

app = FastAPI(title="Pesca Backend API")

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown_event():
    Base.metadata.drop_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API de Pesca ativa!"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(vessel_router)
app.include_router(document_router)
