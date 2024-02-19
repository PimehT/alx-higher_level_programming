#!/usr/bin/python3
"""
Delete all entries that have 'a' in their name
"""
from sqlalchemy import create_engine, delete
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

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()

    session.close()
