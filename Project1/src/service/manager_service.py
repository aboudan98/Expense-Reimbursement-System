import src.doa.manager_doa as m_doa
from json import dumps
from src.models.manager import Manager, ManagerEncoder
from src.models.reimbursement import Reimbursement, ReimbursementEncoder

def validate_manager_info(username, password):
    return m_doa.validate_manager_info(username, password)

def get_manager_data(username, password):
    db_managers = m_doa.get_manager_data(username, password)
    manager_dict = {}
    # parsing through the returned values from the dao to jsonify it
    for managers in db_managers:
        manager_dict[0] = Manager(managers[0], managers[1], managers[2])
    my_json = dumps(manager_dict[0], cls=ManagerEncoder)
    return my_json

def get_all_user_reimbursements():
    db_clients = m_doa.get_all_user_reimbursements()
    reimbursement_dict = {}
    # parsing through the returned values from the dao to jsonify it
    for reimbursements in db_clients:
        reimbursement_dict[reimbursements[0]] = Reimbursement(reimbursements[0], reimbursements[1], reimbursements[2],
                                                              reimbursements[3], reimbursements[4])
    my_json = dumps(reimbursement_dict, cls=ReimbursementEncoder)
    return my_json

def change_reimbursement_status(reimburs_id, decision):
    return m_doa.change_reimbursement_status(reimburs_id, decision)

def get_most_requests():
    return m_doa.get_most_requests()

def get_most_spent():
    return m_doa.get_most_spent()