#!/usr/bin/python3
"""
List all City obj from database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import State, Base
from model_city import City
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

    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
