#!/usr/bin/python3
"""
This module prints the first State object
from the database hbtn_0e_6_usa
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

    # query first python instance in database
    state_obj = session.query(State).order_by(State.id).first()
    if state_obj:
        print("{:d}: {:s}".format(state_obj.id, state_obj.name))
    else:
        print("Nothing")
