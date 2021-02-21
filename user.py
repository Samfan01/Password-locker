class User:
    
    '''
    Class that generates new instances of users.
    '''
    
    user_list = []
    
    def __init__(self,username,password):
  
    
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        save_user method saves user objects into the user_list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method that deletes a saved user
        '''
        User.user_list.remove(self)
        
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in the username and returns a user that matches that username
        
        Args:
            username:username to search for
        Returns:
            User that matches the username.
        '''
        
        for user in cls.user_list:
            if user.username == username:
                return user
    
    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists in the user-list
        Args:
            username:username to search if it exists
        Returns:
            Boolean: True or False depending on the result
        '''
        for user in cls.user_list:
            if user.username == username:
                return True
        
        return False 
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
    