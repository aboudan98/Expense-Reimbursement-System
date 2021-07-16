import werkzeug.exceptions
from src.app import flask_app
from src.models.user import UserEncoder
from json import dumps
import logging
from flask import request, Response, redirect
import src.doa.user_doa as user_doa
import src.service.user_service as u_service
import src.service.manager_service as m_service
# we also need to import the app
logging.basicConfig(filename='logins.log', level=logging.INFO)

# TODO: work on figuring out how js manipulates clicking a button
# TODO: figure out how to get data from a flask api that holds data about types of reimbursements
# TODO: figure out how to get data for a certain user
# TODO: figure out a statisticHello this is Amr I esnt  for a manager
# TODO: Work on manager and user views
# TODO: figure out how to get data for the manager
# TODO: add a dropdown to select whether its a user or a manager
# this might be able to work. Might just need some time to get used to. This is another way
# of using the keyboard but it seems like its the worst way of using it?
# or is it because so far i havent made that many typos. Dont know tho so maybe we can
# do some more experementation with it=
username = ''
password = ''
manager_log_in = False


@flask_app.route('/login.html', methods=['POST'])
def login():
    # use name attribute to get it
    global username
    username = request.form.get('username')
    global password
    password = request.form.get('password')
    global manager_log_in
    manager_log_in = False
    if u_service.validate_user_info(username, password):
        return redirect('http://localhost:5000/user-home-view.html')
    elif m_service.validate_manager_info(username, password):
        manager_log_in = True
        return redirect('http://localhost:5000/manager-home-view.html')
    else:
        return redirect('http://localhost:5000/login.html')

@flask_app.route('/reimbursement-request', methods=['POST'])
def get_reimbursement_request():
    reimb_reason = request.form.get('reason')
    reimb_amount = request.form.get('reimbursement-amount')
    u_service.add_reimbursement(username, password, reimb_reason, reimb_amount)
    return redirect('http://localhost:5000/user-reimbursement-view.html')


@flask_app.route('/login-user-info', methods=['GET'])
def get_user_name():
    global manager_log_in
    logging.info(manager_log_in)
    if manager_log_in:
        return m_service.get_manager_data(username, password)
    return u_service.get_user_data(username, password)


@flask_app.route('/users/reimbursements', methods=['GET'])
def find_all_reimbursements():
    return u_service.get_all_user_reimbursements(username, password)

@flask_app.route('/all-reimbursements', methods=['GET'])
def find_all_user_reimbursements():
    returned = m_service.get_all_user_reimbursements()
    logging.info(returned)
    return returned

@flask_app.route('/reimbursement-approval', methods=['POST'])
def receive_approval():
    reimburs_id = request.form.get('reimbursement-id')
    decision = request.form.get('decision-id')
    decision_lower = decision.lower()
    if decision_lower != 'approved' and decision_lower != 'denied' and decision_lower != 'deny' \
            and decision_lower != 'approve':
        return redirect('/manager-reimbursement-view.html')
    if decision[0].lower() == 'a':
        returned = m_service.change_reimbursement_status(reimburs_id, 'Approved')
    else:
        returned = m_service.change_reimbursement_status(reimburs_id, 'Denied')
    logging.info(returned)
    return redirect('/manager-reimbursement-view.html')

@flask_app.route('/most-requests', methods=['GET'])
def find_most_requests():
    returned = m_service.get_most_requests()
    logging.info(returned)
    return returned

@flask_app.route('/most-spent', methods=['GET'])
def find_most_spent():
    returned = m_service.get_most_spent()
    logging.info(returned)
    return returned