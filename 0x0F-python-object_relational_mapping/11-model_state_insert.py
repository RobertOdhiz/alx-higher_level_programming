#!/usr/bin/python3
"""
Script that lists all State objects from hbtn_0e_6_usa
username, password and dbname are to be as arguments
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    added_state = session.query(State).filter(State.name == 'Louisiana').one()

    print(added_state.id)

    session.close()
