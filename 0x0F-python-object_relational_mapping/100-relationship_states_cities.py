#!/usr/bin/python3

"""
This module creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
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

    # Alt implementation
    # new_s = State(name="California")
    # new_c = City(name="San Francisco")
    # new_s.cities.append(new_c)
    # session.add(new_s)
    # session.add(new_c)

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
