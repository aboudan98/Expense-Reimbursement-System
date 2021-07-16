from src.utils.dbconfig import get_connection


def get_all_user_reimbursements(username, password):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from users where user_username = ? and user_password = ?", username, password)
        # returned as a collection of sequences (tuples)
        row = db_cursor.fetchall()
    finally:
        db_connection.close()
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from reimbursements where user_id = ?", row[0][0])
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()

    return query_rows


def add_reimbursement(username, password, reimb_reason, reimb_amount):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from users where user_username = ? and user_password = ?", username, password)
        # returned as a collection of sequences (tuples)
        row = db_cursor.fetchall()
    finally:
        db_connection.close()
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("insert into reimbursements values(default, ?, ?, 'pending', ?);", reimb_amount, reimb_reason, row[0][0])
        # returned as a collection of sequences (tuples)
        db_connection.commit()
    finally:
        db_connection.close()


def validate_user_info(username, password):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from users where user_username = ? and user_password = ?", username, password)
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()
    if query_rows == []:
        return False
    else:
        return True

def get_user_data(username, password):
    try:
        db_connection = get_connection()
        db_cursor = db_connection.cursor()
        db_cursor.execute("select * from users where user_username = ? and user_password = ?", username, password)
        # returned as a collection of sequences (tuples)
        query_rows = db_cursor.fetchall()
    finally:
        db_connection.close()
    return query_rows
