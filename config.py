import psycopg2.pool

dbconfig = {
    "host": "127.0.0.1",
    "port": "5432",
    "user": "postgres",
    "password": "1234",
    "database": "erpsol"
}

def begin():
    conn = psycopg2.connect(**dbconfig)
    return conn

class PostgresSQLPool(object):
    def __init__(self):
        self.pool = self.create_pool()

    def create_pool(self, minconn=1, maxconn=0):
        pool = psycopg2.pool.ThreadedConnectionPool(
           # pool_name=pool_name,
           # pool_size=pool_size,
            minconn=minconn,
            maxconn=maxconn,
            **dbconfig
        )
        return pool

    def close(self, conn, cursor):
        cursor.close()
        conn.close()

    def call_procedure(self, procedure, args=None, commit=False):
        conn = self.pool.getconn()
        cursor = conn.cursor()

        if args:
            cursor.callproc(procedure, args)
        else:
            cursor.callproc(procedure)

        if commit:
            conn.commit()
            self.close(conn, cursor)
            return cursor
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res

    def execute(self, sql, args=None, commit=False):
        conn = self.pool.getconn()
        cursor = conn.cursor()
        try:
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)

            if commit:
                conn.commit()
                #self.close(conn, cursor)
                #return cursor
        except Exception as e:
            conn.rollback()
            raise e
            print(str(e))
        finally:
            if commit:
                self.close(conn,cursor)
            else:
                res = cursor.fetchall()
                self.close(conn, cursor)
                return res

    def executemany(self, sql, args, commit=True):
        conn = self.pool.getconn()
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        if commit:
            conn.commit()
            self.close(conn, cursor)
            return None
        else:
            res = cursor.fetchall()
            self.close(conn, cursor)
            return res

if __name__ == "__main__":
    db_pool = PostgresSQLPool()
