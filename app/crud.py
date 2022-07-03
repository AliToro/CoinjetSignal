from sqlalchemy.orm import Session

from . import models, schemas


def get_signal(db: Session, signal_id: int):
    return db.query(models.Signal).filter(models.Signal.id == signal_id).first()


def get_signals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Signal).offset(skip).limit(limit).all()


def create_signal(db: Session, signal: schemas.SignalCreate):
    db_signal = models.Signal(full_text=signal.full_text, telegram_chat_id=signal.telegram_chat_id,
                              telegram_chat_title=signal.telegram_chat_title,
                              pair=signal.pair, stop=signal.stop)
    db.add(db_signal)
    db.commit()
    db.refresh(db_signal)
    return db_signal
