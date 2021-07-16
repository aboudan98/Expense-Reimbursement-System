from src.utils.dbconfig import get_connection

def validate_manager_info(username, password):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from managers where manager_username = ? and manager_password = ?", username, password)
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()
    if query_rows == []:
        return False
    else:
        return True


def get_manager_data(username, password):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from managers where manager_username = ? and manager_password = ?", username, password)
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()
    return query_rows

def get_all_user_reimbursements():
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from reimbursements")
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()

    return query_rows

def change_reimbursement_status(reimburs_id, decision):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("update reimbursements set reimbursement_status = ? where reimbursement_id = ?", decision, reimburs_id)
        # returned as a collection of sequences (tuples)
        db_connection.commit()
    finally:
        db_connection.close()


def get_most_requests():
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from users")
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()
    try:
        max_requests = -1000
        max_user = 0
        for user in query_rows:
            db_connection = get_connection()
            db_cursor = db_connection.cursor()
            db_cursor.execute("select count(reimbursement_id) from reimbursements where user_id = ?", user[0])
            # returned as a collection of sequences (tuples)
            row = db_cursor.fetchall()
            if row[0][0] > max_requests:
                max_requests = row[0][0]
                max_user = user
    finally:
        db_connection.close()
    return {"max_user":max_user[1], "max_requests":max_requests}

def get_most_spent():
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from users")
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()
    try:
        max_spent = -1000
        max_user = 0
        for user in query_rows:
            db_connection = get_connection()
            db_cursor = db_connection.cursor()
            db_cursor.execute("select SUM(reimbursement_amount) from reimbursements where user_id = ?", user[0])
            # returned as a collection of sequences (tuples)
            row = db_cursor.fetchall()
            if row[0][0] == None:
                continue
            if row[0][0] > max_spent:
                max_spent = row[0][0]
                max_user = user
    finally:
        db_connection.close()
    return {"max_user":max_user[1], "max_spent":max_spent}
