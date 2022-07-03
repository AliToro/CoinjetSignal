from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/signals/", response_model=schemas.Signal)
def create_signal(signal: schemas.SignalCreate, db: Session = Depends(get_db)):
    db_signal = crud.get_signal_by_email(db, email=signal.email)
    if db_signal:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_signal(db=db, signal=signal)


@app.get("/signals/", response_model=List[schemas.Signal])
def read_signals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    signals = crud.get_signals(db, skip=skip, limit=limit)
    return signals


@app.get("/signals/{signal_id}", response_model=schemas.Signal)
def read_signal(signal_id: int, db: Session = Depends(get_db)):
    db_signal = crud.get_signal(db, signal_id=signal_id)
    if db_signal is None:
        raise HTTPException(status_code=404, detail="Signal not found")
    return db_signal

