#!/usr/bin/python3
"""
Script that lists all City objects from hbtn_0e_6_usa
username, password and dbname are to be as arguments
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    cities = session.query(State, City)\
                    .filter(State.id == City.state.id)

    for item in cities:
        print("{}: ({}) {}".format(item.State.name,
              item.City.id, item.City.name))

    session.close()
