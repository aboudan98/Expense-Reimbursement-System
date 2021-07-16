import src.doa.manager_doa as m_dao
import unittest

class UserDoaTest(unittest.TestCase):
    def test_validate_manager_info_correct(self):
        self.assertEqual(m_dao.validate_manager_info('manager1', 'password'), True)

    def test_validate_manager_info_wrong(self):
        self.assertEqual(m_dao.validate_manager_info('Wrong', 'Input'), False)

    def test_get_manager_data_type(self):
        self.assertIsInstance(m_dao.get_manager_data('manager1', 'password'), list)

    def test_get_manager_data_length(self):
        self.assertGreater(len(m_dao.get_manager_data('manager1', 'password')), 0)

    def test_get_all_user_reimbursements_type(self):
        self.assertIsInstance(m_dao.get_all_user_reimbursements(), list)

    def test_get_all_user_reimbursements_length(self):
        self.assertGreater(len(m_dao.get_all_user_reimbursements()), 0)

    def test_get_most_requests_type(self):
        self.assertIsInstance(m_dao.get_most_requests(), dict)

    def test_get_most_requests_length(self):
        self.assertGreater(len(m_dao.get_all_user_reimbursements()), 0)

    def test_get_most_spent_type(self):
        self.assertIsInstance(m_dao.get_most_spent(), dict)

    def test_get_most_spent_length(self):
        self.assertGreater(len(m_dao.get_most_spent()), 0)