from flask import Flask, render_template, request
from dbmodels import *
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    flights = Volo.query.all()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes.")

    # Prompt user to choose a flight.
    flight_id = int(input("\nFlight ID: "))
    flight = Volo.query.get(flight_id)

    # Make sure flight is valid.
    if flight is None:
        print("Error: No such flight.")
        return

    passengers = Passeggero.query.filter_by(id_volo=flight_id).all()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger)
    if len(passengers) == 0:
        print("No passengers.")


if __name__ == "__main__":
    with app.app_context():
        main()
