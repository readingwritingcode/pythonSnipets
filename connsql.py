'''
    Connection to a database in postgresql employed api python.

    CREATE A NEW DATABASE
    First, log in to the PostgreSQL database server using any client tool
    such as pgAdmin or psql.

    Second, use the following statement to create a new database named suppliers
    in the PostgreSQL database server.

    CREATE DATABASE suppliers.

    CONNECT TO THE POSTGRESSQL DATABASE
    create file name database.ini file, with following lines:

    [postgresql]
    host=localhost
    database=suppliers
    user=postgres
    password=SecurePas$1

    this file is read with the script config.py

from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):

    #create a parser

    parser = ConfigParser()

    #read config file

    parser.read(filename)

    #get section, default to postgresql

    db = {}
    
    if parser.has_section(section):
        
        params = parser.items(section)

        for param in params:

            db[param[0]] = param[0]
    else:

        raise Exception('Section {0] not found in the {1}'.format(section, filename)

    return db
'''

'''The following connect function connects to the suppliers database and prints
   out the Postgressql database version'''

import psycopg2

from config import config

def connect():

    '''connect to the postgresql database server'''

    conn = None

    try:
        # read connection parameters

        params = config()

        # connect to the postgressql database server

        print('connection to the postgresql database ...')

        conn = psycopg2(**params)

        # create a cursor

        cur = conn.cursor()

        # execute a statement

        print('postgrql database version:')

        cur.execute('SELECT version()')

        # display the postgresql database server version

        db_version = cur.fetchone()

        print(db_version)

        #close the communication with the postgresql

        cur.close()
        
    except(Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:
            
            conn.close()
            
            print('Database connection closed.')

if __name__ == '__main__':

    connect()
