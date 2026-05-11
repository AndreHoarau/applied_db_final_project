import pymysql

def find_speaker(name):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='appdbproj',
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = db.cursor()

    sql = """
    SELECT 
        s.speakerName,
        s.sessionTitle,
        r.roomName
    FROM session s
    JOIN room r ON s.roomID = r.roomID
    WHERE s.speakerName LIKE %s
    """

    cursor.execute(sql, ("%" + name + "%",))

    result = cursor.fetchall()

    db.close()

    return result
print("test")