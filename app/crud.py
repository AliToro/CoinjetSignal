from sqlalchemy.orm import Session

from . import models, schemas


def get_signal(db: Session, signal_id: int):
    return db.query(models.Signal).filter(models.Signal.id == signal_id).first()


def get_signal_by_email(db: Session, email: str):
    return db.query(models.Signal).filter(models.Signal.email == email).first()


def get_signals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Signal).offset(skip).limit(limit).all()


def create_signal(db: Session, signal: schemas.SignalCreate):
    fake_hashed_password = signal.password + "notreallyhashed"
    db_signal = models.Signal(email=signal.email, hashed_password=fake_hashed_password)
    db.add(db_signal)
    db.commit()
    db.refresh(db_signal)
    return db_signal
