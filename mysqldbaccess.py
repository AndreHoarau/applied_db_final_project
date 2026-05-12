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

def add_attendee(id, name, dob, gender, id_att_comp):

    db = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='appdbproj',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:

            cursor = db.cursor()

            # -----------------------------
            # 1. Check if Attendee ID exists
            # -----------------------------
            cursor.execute(
                "SELECT attendeeID FROM attendee WHERE attendeeID = %s",
                (id,)
            )

            if cursor.fetchone():
                print("Error: Attendee ID already exists")
                return

            # -----------------------------
            # 2. Validate gender
            # -----------------------------
            if gender not in ["Male", "Female"]:
                print("Error: Gender must be Male/Female")
                return

            # -----------------------------
            # 3. Check Company exists
            # -----------------------------
            cursor.execute(
                "SELECT companyID FROM company WHERE companyID = %s",
                (id_att_comp,)
            )

            if not cursor.fetchone():
                print(f"Company ID {id_att_comp} does not exist")
                return

            # -----------------------------
            # 4. Insert attendee
            # -----------------------------
            sql = """
            INSERT INTO attendee 
            (attendeeID, attendeeName, attendeeDOB, attendeeGender, attendeeCompanyID)
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(sql, (id, name, dob, gender, id_att_comp))
            db.commit()

            print("Attendee successfully added")

    except pymysql.MySQLError as e:
        print("Database error:", e)

    finally:
        db.close()

def get_name_by_id(att_id):
    db = pymysql.connect(
        host='localhost', user='root', password='root', db='appdbproj',
        cursorclass=pymysql.cursors.DictCursor
    )
    cursor = db.cursor()
    sql = "SELECT attendeeName FROM attendee WHERE attendeeID = %s"
    cursor.execute(sql, (att_id,))
    result = cursor.fetchone()
    db.close()
    return result['attendeeName'] if result else None
