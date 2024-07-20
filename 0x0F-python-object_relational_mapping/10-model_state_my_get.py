#!/usr/bin/python3
"""
Print id of object that has the given search name
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State
import sys

if __name__ == "__main__":
    user_n = sys.argv[1]
    pass_w = sys.argv[2]
    data_b = sys.argv[3]
    state_n = sys.argv[4]
    engine_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        engine_str.format(user_n, pass_w, data_b), pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    session = Session(engine)

    row = session.query(State).filter(State.name == state_n).first()
    if not row:
        print('Not found')
    else:
        print(f"{row.id}")
    session.close()
