import unittest
from unittest.mock import Mock
from flask import Response
import src.doa.user_doa as u_doa
import src.models.user as user

# testing the functionality of the dao layer for clients
class UserDoaTest(unittest.TestCase):
    def test_get_all_user_reimbursements_return(self):
        # makes sure the returned is either a response or a list and that its length is more than 0
        self.assertIsInstance(u_doa.get_all_user_reimbursements('James', 'password'), list)

    def test_get_all_user_reimbursements_length(self):
        self.assertGreater(u_doa.get_all_user_reimbursements('James', 'password').__sizeof__(), 0)

    def test_validate_user_info_correct(self):
        self.assertEqual(u_doa.validate_user_info('James', 'password'), True)

    def test_validate_user_info_wrong(self):
        self.assertEqual(u_doa.validate_user_info('Wrong', 'Input'), False)

    def test_get_user_data_return(self):
        # makes sure the returned is either a response or a list and that its length is more than 0
        self.assertIsInstance(u_doa.get_user_data('James', 'password'), list)

    def test_get_user_data_length(self):
        self.assertGreater(u_doa.get_user_data('James', 'password').__sizeof__(), 0)




