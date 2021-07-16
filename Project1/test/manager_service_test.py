import unittest

from unittest.mock import Mock

#out = object under test
import src.service.manager_service as m_service
import src.doa.manager_doa as m_doa
import src.models.user as user


class UserServiceTest(unittest.TestCase):

    def setUp(self):
        m_doa.get_manager_data = Mock(return_value=[(3, 'manager', 'password')])
        # reimbursement_id, reimbursement_amount, reimbursement_reason, reimbursement_status, user_id
        m_doa.get_all_user_reimbursements = Mock(return_value=[(4, 50, 'Lunch', 'pending', 2)])

    def test_get_manager_data_return(self):
        self.assertEqual(m_service.get_manager_data('user1', 'password')[16], str(3))

    def test_get_manager_data_type(self):
        self.assertIsInstance(m_service.get_manager_data('username', 'password'), str)

    def test_get_manager_data_length(self):
        self.assertGreater(len(m_service.get_manager_data('username', 'password')), 0)

    def test_get_all_user_reimbursements_manager_return(self):
        self.assertEqual(m_service.get_all_user_reimbursements()[2], str(4))

    def test_get_all_user_reimbursements_manager_type(self):
        self.assertIsInstance(m_service.get_all_user_reimbursements(), str)

    def test_get_all_user_reimbursements_manager_length(self):
        self.assertGreater(len(m_service.get_all_user_reimbursements()), 0)