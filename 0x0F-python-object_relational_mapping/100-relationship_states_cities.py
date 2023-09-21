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
    Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)
    session = session()

    nstate = "California"
    ncity = "San Francisco"

    newState = State(name=nstate)
    newCity = City(name=ncity)
    newState.cities = [newCity]
    session.add(newState)
    session.commit()
    session.close()
