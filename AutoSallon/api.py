from fastapi import FastAPI, HTTPException
from sqlalchemy import func

from database import SessionLocal, init_db
from models import Car
from schemas import CarCreate, CarRead

app = FastAPI(title="AutoSallon API", version="1.0.0")


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/cars", response_model=list[CarRead])
def list_cars() -> list[CarRead]:
    with SessionLocal() as session:
        cars = session.query(Car).order_by(Car.id.desc()).all()
        return cars


@app.post("/cars", response_model=CarRead)
def create_car(payload: CarCreate) -> CarRead:
    with SessionLocal() as session:
        car = Car(**payload.model_dump())
        session.add(car)
        session.commit()
        session.refresh(car)
        return car


@app.get("/summary")
def summary() -> dict[str, float | int]:
    with SessionLocal() as session:
        total = session.query(func.count(Car.id)).scalar() or 0
        avg_price = session.query(func.avg(Car.price)).scalar() or 0.0
        newest_year = session.query(func.max(Car.year)).scalar() or 0

    return {
        "total_cars": int(total),
        "average_price": round(float(avg_price), 2),
        "newest_year": int(newest_year),
    }
