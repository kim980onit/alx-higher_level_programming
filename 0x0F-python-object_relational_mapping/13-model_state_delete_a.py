#!/usr/bin/python3
"""
    A script that deletes all State objects from hbtn_0e_6_usa that conatin
    the letter a
    Username, password and dbname wil be passed as arguments to the script.
"""


from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.contains('a'))
    if states is not None:
        for state in states:
            session.delete(state)

            session.commit()

            session.close()
