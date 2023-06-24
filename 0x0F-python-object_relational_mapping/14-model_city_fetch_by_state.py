#!/usr/bin/python3
"""
Prints all city objects from the database.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    city_objs = session.query(State.name, City.name).join(
            City, City.state_id == State.id).order_by(City.id).all()

    for city in city_objs:
        print(f"{city.state.name}: ({city.id} {city.name})")
