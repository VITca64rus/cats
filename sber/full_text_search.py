import psycopg2
from psycopg2 import OperationalError


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
    except OperationalError:
        pass
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
                           f'setweight(to_tsvector(CAST(age AS CHAR(15))),'
                           f'\'D\') @@ plainto_tsquery(\'{query}\')'
                           f'ORDER BY '
                           f'ts_rank(setweight(to_tsvector(name), \'A\') || '
                           f'setweight(to_tsvector(info), \'C\') ||'
                           f'setweight(to_tsvector(breed), \'B\') || '
                           f'setweight(to_tsvector(CAST(age AS CHAR(15))),'
                           f'\'D\'), plainto_tsquery(\'{query}\')) DESC) '
                           f'as foo;')
        else:
            cursor.execute(f'SELECT * FROM (SELECT * FROM cat WHERE '
                           f'to_tsvector(name) || to_tsvector(info) || '
                           f'to_tsvector(breed) || to_tsvector(CAST(age '
                           f'AS CHAR(15))) @@ plainto_tsquery(\'{query}\')) a'
                           f's foo ORDER BY {sort};')
        res = cursor.fetchall()
        for i in res:
            result.append({'id': i[0], 'name': i[1], 'age': i[2],
                           'info': i[3], 'breed': i[4], 'photo': i[5]})
        return result
    except OperationalError:
        return result
