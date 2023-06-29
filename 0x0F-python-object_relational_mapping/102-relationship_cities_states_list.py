#!/usr/bin/python3

"""
Use table relationship to access and print city and state
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # use table relationship to access and print city and state
    rows = session.query(City).order_by(City.id).all()
    for city in rows:
        print(f"{city.id}: {city.name} -> {city.state.name}")
