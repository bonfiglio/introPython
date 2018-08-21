from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Flight(Base):
    """ SQL COMMAND :
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);
It is important that you import your models after initializing the db object
TABLE flights <====> db object flights

"""
    __tablename__ = "flights"
    id = Column(Integer, Sequence('flights_seq'), primary_key=True)
    origin = Column(String(20), nullable=False)
    destination = Column(String(20), nullable=False)
    duration = Column(Integer, nullable=False)

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def __repr__(self):
        return ('<flight  %r - %r>' % (self.origin, self.destination))
