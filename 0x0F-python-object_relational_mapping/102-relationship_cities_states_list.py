#!/usr/bin/python3
"""City Relationship"""

import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()
    quary = session.query(City).join(State)\
        .filter(State.id == City.state_id)\
        .order_by(City.id).all()
    for city in quary:
        print("{}: {} -> {}".
              format(city.id, city.name, city.state.name))

    session.close()
