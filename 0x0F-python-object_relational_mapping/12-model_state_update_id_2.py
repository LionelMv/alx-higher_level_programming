#!/usr/bin/python3
"""
Changes the name of a State object from the database.
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

    changed_state = session.query(State).filter(State.id == 2).first()
    changed_state.name = 'New Mexico'
    session.commit()
