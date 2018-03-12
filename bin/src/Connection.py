"""
    @author: Josue Carbonel
    @date:  3/12/2018
"""

# install pymysql using 'pip install pymysql' in terminal
import pymysql

import Helper


class Connection:
    """
    Connection class
        It helps us to access and manage the database.
    """
    USER = "fc"
    PASSWORD = "fluent_city"
    HOST = "letsdoit.io"
    PORT = 3306
    DATABASE = "fluent_city"

    def __init__(self):
        print("Connection Object created: ")

    def db_connect(self):
        """
        This will connect to our database and will return a connection instance
            otherwise it will return a None object
        :return: Connection conn
        """
        try:
            conn = pymysql.connect(
                user=self.USER,
                passwd=self.PASSWORD,
                host=self.HOST,
                port=self.PORT)

            print("Connected")
            return conn
        except Exception as e:
            print("Oops.. there is some error")
            print(e)
            return None

    def re_build_database(self, app_path):
        # Connects to the database
        conn = self.db_connect()

        try:
            """
            Drops database to delete previous one
            """
            self.drop_database()
        except Exception as e:
            print(e)

        if conn is not None:
            # If connection exists
            cur = conn.cursor()

            # Get the sql file from our assets file and make a tuple
            queries = Helper.get_squema(app_path).split("\n")

            for q in queries:
                # loop multiple queries that are in our sql file
                try:
                    cur.execute(q)  # Execute each query
                except Exception as e:
                    # close connection if some error exists
                    conn.rollback()
                    conn.close()
                    print(e)

            print("Database created")
        else:
            print("No Action was executed")

    def drop_database(self):
        """
        This method will drop the database if exists
        :return:
        """
        conn = self.db_connect()
        if conn is not None:
            cur = conn.cursor()

            q = "DROP DATABASE " + self.DATABASE + ";"

            try:
                cur.execute(q)
            except Exception as e:
                conn.rollback()
                conn.close()
                print(e)
            print("Database Dropped")
        else:
            print("No Action was executed, because we couldn't connect to the database.")
