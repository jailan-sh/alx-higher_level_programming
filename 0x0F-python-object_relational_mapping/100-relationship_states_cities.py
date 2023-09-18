#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()
    records = session.query(State, City)\
        .join(City, City.state_id == State.id)\
        .order_by(City.id).all()
    for state, city in records:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
