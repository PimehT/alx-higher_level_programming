#!/usr/bin/python3
"""
List all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    user_n = sys.argv[1]
    pass_w = sys.argv[2]
    data_b = sys.argv[3]
    engine_str = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        engine_str.format(user_n, pass_w, data_b), pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    query = select(State)
    result = session.execute(query)
    rows = result.fetchall()

    for row in rows:
        print("{}".format(row))

    session.close()
