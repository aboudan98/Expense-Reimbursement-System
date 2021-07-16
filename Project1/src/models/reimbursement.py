from json import JSONEncoder


class Reimbursement:
    # constructor for initializing a user
    def __init__(self, reimbursement_id, reimbursement_amount, reimbursement_reason, reimbursement_status, user_id):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_amount = reimbursement_amount
        self.reimbursement_reason = reimbursement_reason
        self.reimbursement_status = reimbursement_status
        self.user_id = user_id

class ReimbursementEncoder(JSONEncoder):
    def default(self, reimbursement):
        if isinstance(reimbursement, Reimbursement):
            return reimbursement.__dict__
        else:
            # if something goes wrong just fall back to the parent implementation
            return super().default(self, reimbursement)