import psycopg2
from psycopg2 import OperationalError
from werkzeug.security import generate_password_hash


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_read_query(connection, query, sort):
    cursor = connection.cursor()
    result = []
    try:
        if sort == "name":
            cursor.execute(f'SELECT * FROM ('
                           f'SELECT * FROM cat WHERE '
                                f'setweight(to_tsvector(name), \'A\') || '
                                f'setweight(to_tsvector(info), \'C\') || '
                                f'setweight(to_tsvector(breed), \'B\') || '
                                f'setweight(to_tsvector(CAST(age AS CHAR(15))), \'D\') @@ plainto_tsquery(\'{query}\')'
                           f'ORDER BY '
                                f'ts_rank(setweight(to_tsvector(name), \'A\') || '
                                f'setweight(to_tsvector(info), \'C\') ||'
                                f'setweight(to_tsvector(breed), \'B\') || '
                                f'setweight(to_tsvector(CAST(age AS CHAR(15))), \'D\'), '
                                f'plainto_tsquery(\'{query}\')) DESC) as foo;')
        else:
            cursor.execute(f'SELECT * FROM (SELECT * FROM cat WHERE to_tsvector(name) || to_tsvector(info) || '
                           f'to_tsvector(breed) || to_tsvector(CAST(age AS CHAR(15))) @@ plainto_tsquery(\'{query}\')) a'
                           f's foo ORDER BY {sort};')
        res = cursor.fetchall()
        for i in res:
            result.append({'id': i[0], 'name': i[1], 'age': i[2], 'info': i[3], 'breed': i[4], 'photo': i[5]})
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        return result
