from flask import Flask, render_template
from database import init_db, db
from models import Car
from scraper import scrape_car_brands
from api_service import get_exchange_rate
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dealership.db'

init_db()

@app.route("/")
def home():
    try:
        # Variables
        exchange_rate = get_exchange_rate()
        brands = scrape_car_brands()

        # Data structure (list of dictionaries)
        car_list = [
            {"brand": "Toyota", "model": "Corolla", "price": 20000, "year": 2022},
            {"brand": "BMW", "model": "X5", "price": 50000, "year": 2023},
            {"brand": "Audi", "model": "A4", "price": 40000, "year": 2021},
        ]

        # Loop + Conditional + Database insert
        for car in car_list:
            if not Car.query.filter_by(model=car["model"]).first():
                new_car = Car(
                    brand=car["brand"],
                    model=car["model"],
                    price=car["price"],
                    year=car["year"]
                )
                db.session.add(new_car)

        db.session.commit()

        # Data manipulation with pandas
        cars = Car.query.all()
        car_dicts = [c.to_dict() for c in cars]
        df = pd.DataFrame(car_dicts)

        if exchange_rate:
            df["price_eur"] = df["price"] * exchange_rate

        total_cars = len(df)

        return render_template(
            "index.html",
            cars=cars,
            total=total_cars,
            exchange=exchange_rate,
            brands=brands
        )

    except Exception as e:
        return f"Application Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)