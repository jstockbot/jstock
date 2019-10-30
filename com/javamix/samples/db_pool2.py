import mysql.connector
from mysql.connector import Error
from mysql.connector.connection import MySQLConnection
from mysql.connector import pooling

try:
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="pynative_pool", pool_size=5,
                                                                  pool_reset_session=True,
                                                                  host = 'localhost',
                                                                  database = 'jstock',
                                                                  user = 'javamix',
                                                                  password = 'javamix')
    