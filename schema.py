from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class ShowerBase(BaseModel):
    name: str


class ShowerCreate(ShowerBase):
    description: str
    observation_start_date: date
    observation_end_date: date
    alpha: int
    beta: int
    pick_date: date


class Shower(ShowerBase):
    id: int
    observation_start_date: date
    observation_end_date: date
    alpha: int
    beta: int
    pick_date: date

    class Config:
        orm_mode = True
