#!/usr/bin/python3
"""
List first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    user_n = sys.argv[1]
    pass_w = sys.argv[2]
    data_b = sys.argv[3]
    engine_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        engine_str.format(user_n, pass_w, data_b), pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).order_by(State.id).first()

    if (state):
        print("{}: {}".format(state.id, state.name))
    else:
        print('')

    session.close()
