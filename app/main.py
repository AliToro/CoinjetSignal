import logging
from collections import deque
from datetime import datetime
from time import sleep
from typing import List

from fastapi import Depends, FastAPI, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from starlette import status

from . import crud, models, schemas, log
from .database import SessionLocal, engine
from .signal_status import SignalStatus

models.Base.metadata.create_all(bind=engine)
failed_signals_queue = deque()
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/signals/", response_model=schemas.Signal)
async def create_signal(signal: schemas.SignalCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    signal.received_at = datetime.now()
    signal.status = SignalStatus.Received.value
    if signal.is_futures:
        if signal.is_short is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Field 'is_short' is mandatory when signal is future!")
        if signal.leverage is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Field 'leverage' is mandatory when signal is future!")
    created_signal = crud.create_signal(db=db, signal=signal)
    background_tasks.add_task(send_signal, signal)
    return created_signal


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


def send_signal(signal: schemas.SignalCreate):
    logging.info("Start sending the '{}' signal".format(signal.full_text))
    sleep(10)
    if False:
        failed_signals_queue.append(signal)
    logging.info("Signal sent successful!")

