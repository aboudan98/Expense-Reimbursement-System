from json import dumps
import src.doa.user_doa as udoa
from src.models.user import User, UserEncoder
from src.models.reimbursement import Reimbursement, ReimbursementEncoder

def get_all_user_reimbursements(username,password):
    db_clients = udoa.get_all_user_reimbursements(username, password)
    reimbursement_dict = {}
    # parsing through the returned values from the dao to jsonify it
    for reimbursements in db_clients:
        reimbursement_dict[reimbursements[0]] = Reimbursement(reimbursements[0], reimbursements[1], reimbursements[2], reimbursements[3], reimbursements[4])
    my_json = dumps(reimbursement_dict, cls=ReimbursementEncoder)
    return my_json

def validate_user_info(username, password):
    return udoa.validate_user_info(username, password)


def add_reimbursement(username, password, reimb_reason, reimb_amount):
    return udoa.add_reimbursement(username, password, reimb_reason, reimb_amount)

def get_user_data(username, password):
    db_users = udoa.get_user_data(username, password)
    user_dict = {}
    # parsing through the returned values from the dao to jsonify it
    for users in db_users:
        user_dict[0] = User(users[0], users[1], users[2], list())
    my_json = dumps(user_dict[0], cls=UserEncoder)
    return my_json

