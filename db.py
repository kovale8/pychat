import pymysql.cursors

connection = pymysql.connect(
    host='35.231.133.214',
    user='root',
    password='ybh3DlctYD',
    db='pychat',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def query(sql, values=()):
    result = None

    with connection.cursor() as cursor:
        cursor.execute(sql, values)

        result = cursor.fetchall();

    connection.commit()

    return result
