import pytest
from psycopg2 import DatabaseError
from database import db

class TestConnBd:
    cons = db.config
    
    def test_conn_bd(self):
        conn = db.get_connection()
        assert conn is not None
        conn.close()