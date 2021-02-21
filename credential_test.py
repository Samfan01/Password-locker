import unittest
import user
from credentials import Credential


class TestUser(unittest.TestCase):
    '''
    Test case class for credential class behaviours
    Args:
        unittest.TestCase: TestCase class that will
        help in creatin test cases
    '''
    
    def setUp(self):
        '''
        method to run before each case
        '''
        self.new_credential = Credential('facebook','facebook101')
        
    def tearDown(self):
        '''
        clean up method
        '''
        Credential.credential_list = []
        
    def test_init(self):
        '''
        test to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credential.account_name,'facebook')
        self.assertEqual(self.new_credential.account_password,'facebook101')

    def test_save_credentail(self):
        '''
        test_save_credential to save credentials
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_delete_credential(self):
        '''
        test to see if we can remove credential from list
        '''
        self.new_credential.save_credential()
        test_credential = Credential('Netflix','watch100')
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_find_credential_by_account_name(self):
        '''
        test case to check if we an find credentials using the 
        account name
        '''
        self.new_credential.save_credential()
        test_credential = Credential('Netflix','watch100')
        test_credential.save_credential()
        
        found_credential = Credential.find_by_account_name('Netflix')
        
        self.assertEqual(found_credential.account_password,test_credential.account_password)
    
    
if __name__ == '__main__':
    unittest.main()    
        