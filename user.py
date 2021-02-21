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
    