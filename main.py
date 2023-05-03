from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import schema
import model
from database import engine, SessionLocal
import crud

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def main(request: Request):
    date = datetime.utcnow().isoformat(sep=" ", timespec="seconds")
    context = {"request": request, "message": date, "title": "Home page"}
    return templates.TemplateResponse("home.html", context=context)


@app.post("/create/shower", response_model=schema.Shower)
async def create_shower(shower: schema.ShowerCreate, db: Session = Depends(get_db)):
    db_shower = crud.get_shower_by_name(db, name=shower.name)
    if db_shower:
        raise HTTPException(
            status_code=400, detail="Meteor shower with this name already registered!"
        )
    return crud.create_shower(db, shower=shower)


@app.get("/list/shower/")
async def get_list_shower(request: Request, db: Session = Depends(get_db)):
    showers = crud.get_showers(db=db)
    context = {'request': request, "showers": showers, "title": 'Meteor Showers'}
    return templates.TemplateResponse("meteor_list_shower.html", context=context)


@app.get("/get/shower/{shower_name}", response_model=schema.Shower)
async def get_shower_by_name(request: Request, shower_name: str, db: Session = Depends(get_db)):
    shower = crud.get_shower_by_name(db, shower_name)
    context = {'request': request, 'shower': shower, 'title': shower.name}
    return templates.TemplateResponse('meteor_shower.html', context=context)


@app.delete("/delete/meteor_shower/{meteor_shower_name}")
async def delete_shower(meteor_shower_name: str, db: Session = Depends(get_db)):
    crud.delete_meteor_shower_by_name(db, meteor_shower_name)
