from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///./dealership.db"


class Base(DeclarativeBase):
    pass


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db() -> None:
    from models import Car

    Base.metadata.create_all(bind=engine)

    # Seed minimal data once for a nicer first UI experience.
    with SessionLocal() as session:
        has_data = session.query(Car).first() is not None
        if has_data:
            return

        session.add_all(
            [
                Car(brand="Toyota", model="Corolla", year=2022, price=21000),
                Car(brand="BMW", model="X5", year=2023, price=56000),
                Car(brand="Audi", model="A4", year=2021, price=42000),
                Car(brand="Tesla", model="Model 3", year=2024, price=47000),
            ]
        )
        session.commit()
