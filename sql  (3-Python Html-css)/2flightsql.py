# mysql://db4free.net:3306/dbrekse
'''
The SQLAlchemy Object Relational Mapper
presents a method of associating user-defined Python classes with database tables,
and instances of those classes (objects) with rows in their corresponding tables.
'''
scott = input("User Name:")
tiger = input("Password:")
import pymysql

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To connect  with the database we use create_engine(): ex..create_engine('sqlite:///:memory:', echo=True)
some_engine = create_engine(f"mysql+pymysql://{scott}:{tiger}@db4free.net:3306/dbrekse?charset=utf8mb4", echo=True)
# some_engine is an instance of Engine it represents the core interface to the database,
# adapted through a dialect that handles the details of the database

# ORM needs the configurational process, it starts by describing the database tables
Base = declarative_base()


def main():
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

    def creadbflights():
        dbServerName = "db4free.net"
        dbUser = scott
        dbPassword = tiger
        dbName = "dbrekse"
        charSet = "utf8mb4"
        cusrorType = pymysql.cursors.DictCursor
        connectionObject = pymysql.connect(host=dbServerName, port=3306, user=dbUser, password=dbPassword,
                                           db=dbName, charset=charSet, cursorclass=cusrorType)
        try:
            # Create a cursor object
            cursorObject = connectionObject.cursor()
            # SQL query string
            # sqlQuery = "CREATE TABLE IF NOT EXISTS Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"
            sqlQuery = "CREATE TABLE flights (" \
                       " id SERIAL PRIMARY KEY, " \
                       "origin VARCHAR(128) NOT NULL," \
                       " destination VARCHAR(128) NOT NULL," \
                       " duration INTEGER NOT NULL )"
            # Execute the sqlQuery
            cursorObject.execute(sqlQuery)
            # SQL query string
            # sqlQuery = "SELECT id, firstname , lastname FROM MyGuests"
            sqlQuery = "show tables"
            # Execute the sqlQuery
            cursorObject.execute(sqlQuery)
            # Fetch all the rows
            rows = cursorObject.fetchall()
            for row in rows:
                print(row['Tables_in_dbrekse'], type(row))
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            connectionObject.close()

    class Flight(Base):

        __tablename__ = "flights"
        id = Column(Integer, Sequence('flights_seq'), primary_key=True)
        origin = Column(String(20), nullable=False)
        destination = Column(String(20), nullable=False)
        duration = Column(Integer, nullable=False)

        # id = db.Column(db.Integer, primary_key=True)
        # username = db.Column(db.String(80), unique=True)
        # email = db.Column(db.String(120), unique=True)

        def __init__(self, origin, destination, duration):
            self.origin = origin
            self.destination = destination
            self.duration = duration

        def __repr__(self):
            return ('<flight  %r - %r>' % (self.origin, self.destination))

    # creadbflights() VECCHIA SISTEMA : MANDO COMANDO DI CREAZIONE DELLA TABELLA
    Flight.metadata.create_all(some_engine, checkfirst=True)
    # Now  we define a Session class which will serve as a factory for new Session objects
    # session is the ORM’s “handle” to the database

    Session = sessionmaker(bind=some_engine)
    session = Session()

    # we add() it to our session a new flight:
    volo = Flight('New York', 'London', 415)
    session.add(volo)
    nyqueryFlights = session.query(Flight).filter_by(origin='New York') \
        # .first()
    print(nyqueryFlights)
    ny_lista = nyqueryFlights.all()
    print(ny_lista)
    session.commit()
    # voli = Flight.
    # print(voli)


if __name__ == "__main__":
    main()
