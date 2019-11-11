from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

# Name of database
DB_NAME = 'HSM Thesis'

////////////////////////////
// creating tables
///////////////////////////
// STOCK INFO TABLE
TABLES = {}
TABLES['stocks'] = (
	" CREATE TABLE 'stocks' ("							// creates stocks table
	"	'stock_name' varchar(6) NOT NULL,"					// stock names
	"	'dates' date NOT NULL,"							// dates
	"	'closing_price' int() NOT NULL,"					// closing prices for each date for each stock
	" PRIMARY KEY ('stock_name'), UNIQUE KEY 'stock_name' ('stock_name')		// stock names are primary keys and unique keys
	") ENGINE=InnoDB")

// RETURN OF STOCKS TABLE (1ST EQUATION)
TABLES('return_of_stock') = (
	" CREATE TABLE 'return_of_stocks' ("						// creates return of stock table
	"	'return_value_stocks' int() NOT NULL,"					// return of the equation
	"	'day_closing_price' int() NOT NULL,"					// closing prices of start dates
	"	'day_after_closing_price' int() NOT NULL,"				// closing prices of previous day to start dates
	"	REFERENCES 'stocks' ('stock_name'),"
	"	REFERENCES 'stocks' ('dates'),"
	" PRIMARY KEY ('return_value_stocks')"
	") ENGINE=InnoDB")

// TOTAL PORTFOLIO TABLE (2ND EQUATION)
TABLES('total_portfolio') = (
	"CREATE TABLE 'total_portfolio' ("						// creates total portfolio table
	"	'return_of_portfolio' int() NOT NULL,"					// return of equation (return of value + weight of each day added together)
	"	'return_value_stocks' int() NOT NULL,'"					// return value of stocks from RETURN OF STOCK table
	"	'weight_of_stocks' int() NOT NULL,"					// weight of stocks
	" PRIMARY KEY ('return_of_portfolio')"
	"} ENGINE=InnoDB")

////////////////////////////////////////////
// connecting to MySQL
////////////////////////////////////////
cnx = mysql.connector.connect(user='root, database='HSM Thesis')
cursor = cnx.cursor()

////////////////////////////////////////
// inserting data into database tabels
///////////////////////////////////////

// tomorrow = datetime.now().date() + timedelta(days=1)
// ^ can use this for dates in table?

add_stock = ("INSERT INTO stocks

add_start_date =

add_end_date =

add_closing_price =

add_cinfidence level =


# //////////////////////////////////
# // creating database
# /////////////////////////////////
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# error message if something goes wrong
try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# creating tables and printing tables in cmd
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()