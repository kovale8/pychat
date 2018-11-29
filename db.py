import os
import sqlalchemy

user = os.environ.get('CLOUD_SQL_USERNAME')
password = os.environ.get('CLOUD_SQL_PASSWORD')
host = os.environ.get('CLOUD_SQL_HOST')
name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


# When deployed to App Engine, the `GAE_ENV` environment variable will be
# set to `standard`
if os.environ.get('GAE_ENV') == 'standard':
    # If deployed, use the local socket interface for accessing Cloud SQL
    unix_socket = '/cloudsql/{}'.format(connection_name)
    engine_url = 'mysql+pymysql://{}:{}@/{}?unix_socket={}'.format(
        user, password, name, unix_socket)
else:
    # If running locally, use the TCP connections instead
    # Set up Cloud SQL Proxy (cloud.google.com/sql/docs/mysql/sql-proxy)
    # so that your application can use 127.0.0.1:3306 to connect to your
    # Cloud SQL instance
    engine_url = 'mysql+pymysql://{}:{}@{}/{}'.format(
        user, password, host, name)

engine = sqlalchemy.create_engine(engine_url, pool_size=3)


def query(sql, values=()):
    result = None
    cnx = engine.connect()
    cursor = cnx.execute(sql, values)

    # Ignore it complaining about no returned rows.
    try:
        result = cursor.fetchall()
    except Exception:
        pass


    cnx.close()
    return result
