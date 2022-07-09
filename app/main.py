from datetime import datetime
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette import status

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
    signal.received_at = datetime.now()
    signal.status = 0
    if signal.is_futures:
        if signal.is_short is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Field 'is_short' is mandatory when signal is future!")
        if signal.leverage is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Field 'leverage' is mandatory when signal is future!")
    return crud.create_signal(db=db, signal=signal)


@app.get("/signals/", response_model=List[schemas.Signal])
def read_signals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    signals = crud.get_signals(db, skip=skip, limit=limit)
    return signals


@app.get("/signals/{signal_id}", response_model=schemas.Signal)
def read_signal(signal_id: int, db: Session = Depends(get_db)):
    db_signal = crud.get_signal(db, signal_id=signal_id)
    if db_signal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Signal not found")
    return db_signal
