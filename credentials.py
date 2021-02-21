class Credential:
    '''
    class to  create new instances of account credentials
    '''
    credential_list = []
    
    def __init__(self,account_name,account_password):
        '''
        passed three arguments to represent instances of our variables
        '''
        self.account_name = account_name
        self.account_password = account_password
        
    def save_credential(self):
        '''
        method to save credential
        '''
        Credential.credential_list.append(self)
        
    def delete_credential(self):
        '''
        method to delete saved credentials
        '''
        Credential.credential_list.remove(self)