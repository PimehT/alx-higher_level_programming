#!/usr/bin/python3
"""
List all City obj from database hbtn_0e_14_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City
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
    Session = sessionmaker(bind=engine)
    session = Session()

    id = 0

    for state, city in (session.query(State, City)
                        .join(City, State.id == City.state_id)
                        .order_by(City.id)).all():
        if state.id is not id:
            id = state.id
            print(f"{state.id}: {state.name}")
        print(f"\t{city.id}: {city.name}")
