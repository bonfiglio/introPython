# mysql://db4free.net:3306/dbrekse
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

scott = input("User Name:")
tiger = input("Password:")
import pymysql


# engine = create_engine(os.getenv("DATABASE_URL"))
# engine = create_engine(f"mysql+pymysql://{scott}:{tiger}@db4free.net:3306/dbrekse")
# db = scoped_session(sessionmaker(bind=engine))


def main():
    myguests = db.execute("SELECT id, firstname , lastname FROM MyGuests").fetchall()
    for guest in myguests:
        print(f"{guest.id} to {guest.firstname}, {guest.lastname} ")
    # myguests = db.execute("CREATE TABLE flights (id SERIAL PRIMARY KEY,origin "
    #                     "VARCHAR NOT NULL,destination VARCHAR NOT NULL,"
    #                      "duration INTEGER NOT NULL")
    # print(myguests)


if __name__ != "__main__":
    main()

# import pymysql

# Create a connection object
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
    sqlQuery = "CREATE TABLE IF NOT EXISTS Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"
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
