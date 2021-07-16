import unittest

from unittest.mock import Mock

#out = object under test
import src.service.user_service as u_service
import src.doa.user_doa as u_doa
import src.models.user as user


class UserServiceTest(unittest.TestCase):

    def setUp(self):
        u_doa.get_user_data = Mock(return_value=[(2, 'member', 'password', list())])
        # reimbursement_id, reimbursement_amount, reimbursement_reason, reimbursement_status, user_id
        u_doa.get_all_user_reimbursements = Mock(return_value=[(4, 50, 'Lunch', 'pending', 2)])

    def test_get_user_data_return(self):
        self.assertEqual(u_service.get_user_data('user1', 'password')[13], str(2))

    def test_get_user_data_type(self):
        self.assertIsInstance(u_service.get_user_data('username', 'password'), str)

    def test_get_user_data_length(self):
        self.assertGreater(len(u_service.get_user_data('username', 'password')), 0)

    def test_get_all_user_reimbursements_return(self):
        self.assertEqual(u_service.get_all_user_reimbursements('user1', 'password')[2], str(4))

    def test_get_all_user_reimbursements_type(self):
        self.assertIsInstance(u_service.get_all_user_reimbursements('username', 'password'), str)

    def test_get_all_user_reimbursements_length(self):
        self.assertGreater(len(u_service.get_all_user_reimbursements('username', 'password')), 0)