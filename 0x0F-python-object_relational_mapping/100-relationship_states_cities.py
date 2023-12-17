#!/usr/bin/python3
""" 100-relationship_states_cities.py """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    new_state = State(name="California")

    # Create a new City object
    new_city = City(name="San Francisco")

    # Use the cities relationship to link the new city to the new state
    new_state.cities.append(new_city)

    # Add the new state to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
