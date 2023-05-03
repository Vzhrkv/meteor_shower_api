from sqlalchemy import update
from sqlalchemy.orm import Session
from utils import hash_password

from model import User, Shower
from schema import UserCreate, ShowerCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):
    return db.query(User).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_showers(db: Session):
    return db.query(Shower).all()


def get_shower_by_name(db: Session, name: str):
    return db.query(Shower).filter(Shower.name == name).first()


def create_shower(db: Session, shower: ShowerCreate):
    db_shower = Shower(**shower.dict())
    db.add(db_shower)
    db.commit()
    db.refresh(db_shower)
    return db_shower


def delete_meteor_shower_by_name(db: Session, name: str):
    db_shower = get_shower_by_name(name)
    db.delete(db_shower)
    db.commit()
