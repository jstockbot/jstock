import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
from mysql.connector.connection import MySQLConnection

try:
    connection_pool = pooling.MySQLConnectionPool(pool_name="jstockdb_pool",
                                                  pool_size=5,
                                                  pool_reset_session=True,
                                                  host='127.0.0.1',
                                                  database='jstock',
                                                  user='javamix',
                                                  password='javamix')
    print("Printing connection pool properties.")
    print("Connection Pool Name = {}".format(connection_pool.pool_name))
    print("Connection Pool Size = {}".format(connection_pool.pool_size))

    # get connection object from a pool
    connection_obj = connection_pool.get_connection()
    conn = connection_pool.get_connection()

    if connection_obj.is_connected():
        db_info = connection_obj.get_server_info()
        print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_info)
        cursor = connection_obj.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("{} 에 연결됨".format(record))
except Error as e:
    print("Error MySQL Connection Pool : {}".format(e))
finally:
    if(connection_obj.is_connected()):
        cursor.close()
        connection_obj.close()
        print("MySQL Connection is closed!")
