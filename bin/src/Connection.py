import pymysql

import Helper


class Connection:
    USER = "root"
    PASSWORD = ""
    HOST = "127.0.0.1"
    PORT = 3306
    DATABASE = "fluent_city"

    def __init__(self):
        print("Connection Object created: ")

    def db_connect(self):
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
        conn = self.db_connect()
        if conn is not None:
            cur = conn.cursor()

            queries = Helper.get_squema(app_path).split("\n")

            for q in queries:
                try:
                    cur.execute(q)
                except Exception as e:
                    conn.rollback()
                    conn.close()
                    print(e)

            print("Database created")
        else:
            print("No Action was executed")

    def drop_database(self):
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
            print("No Action was executed")
