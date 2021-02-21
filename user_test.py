import unittest
from user import User

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the user 
    class behaviours.
    
    Args:
        unittest.TestCase:TestCase class that helps
        in creating test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test case.
        '''
        self.new_user = User('Samfan01','Therockers001')
        
    def test_init(self):
        '''
        test init test case to test if the object is initialised properly
        '''
        
        self.assertEqual(self.new_user.username,'Samfan01')
        self.assertEqual(self.new_user.password,'Therockers001')
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved
        into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)  
        
if __name__=='__main__':
    unittest.main()
