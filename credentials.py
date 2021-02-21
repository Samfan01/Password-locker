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
    
    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        method that takes in account name and returns 
        credential
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def credential_exists(cls,account_name):
        '''
        Method that checks if the credential exists
        
        Returns:
            Boolean:True or False depending on the result
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True
            
        return False
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list

    
            