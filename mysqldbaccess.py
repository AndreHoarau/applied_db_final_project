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

def find_comp(compid):
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
        c.companyName,
        a.attendeeName,
        a.attendeeDOB,
        s.sessionTitle,
        s.speakerName,
        s.sessionDate,
        r.roomName
    FROM company c
    JOIN attendee a
    ON c.companyID = a.attendeeCompanyID
    JOIN registration reg
        ON a.attendeeID = reg.attendeeID
    JOIN session s
        ON reg.sessionID = s.sessionID
    JOIN room r
        ON s.roomID = r.roomID
    WHERE c.companyID = %s
    """

    cursor.execute(sql, (compid,))

    result = cursor.fetchall()

    db.close()
    return result

def company_exists(compid):

    db = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='appdbproj',
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = db.cursor()

    sql = """
    SELECT companyName
    FROM company
    WHERE companyID = %s
    """

    cursor.execute(sql, (compid,))

    result = cursor.fetchone()

    db.close()

    return result