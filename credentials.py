class Credential:
    '''
    class to  create new instances of account credentials
    '''
    Credential_list = []
    
    def __init__(self,account_name,account_password):
        '''
        passed three arguments to represent instances of our variables
        '''
        self.account_name = account_name
        self.account_password = account_password
        
    