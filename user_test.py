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
     
    def tearDown(self):
        '''
        tearDown method that does clean up after each test runs
        '''
        User.user_list = []
        
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
    
    def test_save_multiple_user(self):
        '''
        test case to test if we can save multiple
        user objects in our user_list.
        '''
        self.new_user.save_user()
        test_user = User('Test','Test001')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_delete_user(self):
        '''
        test case te see if we can remove a user from the user_list
        '''
        
        self.new_user.save_user()
        test_user = User('Test','Test001')
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
        
    def test_find_user_by_username(self):
        '''
        test case to test if we can find a saved user
        by user name and display the information.
        '''
        self.new_user.save_user()
        test_user = User('Test','Test001')
        test_user.save_user()
        
        found_user = User.find_by_username('Test')
        
        self.assertEqual(found_user.password,test_user.password)   
           
if __name__=='__main__':
    unittest.main()
