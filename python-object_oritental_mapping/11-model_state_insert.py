#!/usr/bin/python3
'''
    a script that prints the State object with the name
    passed as argument from database hbtn_0e_6_usa
'''
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
             pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)

    states = session.query(State).filter(State.name == 'Louisiana').first()
    print("{}".format(states.id))
    #if states:
    #   for state in states:
    #       print("{}".format(state.id))
    #else:
    #   print("Not found")
