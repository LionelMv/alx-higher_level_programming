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

    # creates a tuple
    # One implementation
    # cities = session.query(City).join(State).order_by(City.id).all()
    # for city in cities:
    #     print('{}: ({}) {}'.format(city.state.name, city.id, city.name))

    city_query = session.query(State.name, City.id, City.name).\
        filter(City.state_id == State.id).all()

    for city in city_query:
        print(f"{city[0]}: ({city[1]}) {city[2]}")