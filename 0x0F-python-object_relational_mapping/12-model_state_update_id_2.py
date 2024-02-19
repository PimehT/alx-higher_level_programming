#!/usr/bin/python3
"""
Update the name of a state to a new state
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

    new_st = "New Mexico"
    session.query(State).filter(State.id == 2).update({State.name: new_st})
    session.commit()

    session.close()
