#!/usr/bin/python3
"""
Lists state objects containing letter 'a' from the database.
"""

from sys import argv
from model_state import Base, State
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
    state_objs = session.query(State).filter_by(name=argv[4]).first()
    if state_objs:
        print(f"{state_objs.id}")
    else:
        print("Not found")
