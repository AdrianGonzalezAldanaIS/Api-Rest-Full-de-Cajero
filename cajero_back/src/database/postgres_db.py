from psycopg2.pool import ThreadedConnectionPool
from psycopg2 import DatabaseError
from decouple import config
from contextlib import contextmanager

db_config = { "host" : config('PGSQL_HOST'),
                "database" : config('PGSQL_DATABASE'),
                "user" : config('PGSQL_USER'),
                "password" : config('PGSQL_PASSWORD')}

class PostgresDB:
    def __init__(self):
        self.app = None
        self.pool = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.pool = ThreadedConnectionPool(minconn=1, maxconn=30, **db_config)

    @contextmanager
    def get_cursor(self):
        if self.pool is None:
            self.connect()
        con = self.pool.getconn() # type: ignore
        try:
            yield con.cursor()
            con.commit()
        finally:
            self.pool.putconn(con) # type: ignore













