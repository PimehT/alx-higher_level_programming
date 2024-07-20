#!/usr/bin/python3
"""
List all State objects that contain the letter 'a'
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
    engine_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        engine_str.format(user_n, pass_w, data_b), pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    session = Session(engine)

    new_name = "Louisiana"
    new_state = State(name=new_name)
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == new_name).first()
    if state:
        print(f"{state.id}")

    session.close()
