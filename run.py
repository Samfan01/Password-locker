#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import random
import string


def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(username):
    '''
    Function that finds a user by username and returns 
    the user
    '''
    return User.find_by_username(username)
def check_existing_user(username):
    '''
    Function that check if a user exists with that username
    '''
    return user.user_exist(username)
def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()
def create_credential(account_name,account_password):
    '''
    Function to save new account
    '''
    new_account = Credential(account_name,account_password)
    return new_account
def save_credential(credential):
    '''
    for saving credentials
    '''
    credential.save_credential
    
def password_generetor():
    '''
    function to generate password for the user
    '''
    P = string.ascii_uppercase + string.ascii_lowercase + string.digits
    print('Enter the length of your Password ')
    p_length = int(input())
    password = ''.join(random.choices(P, k=p_length))
    
    return password    
def display_credential(credential):
    '''
    function to display credentials
    '''
    return Credential.display_credential()
def delete_credential(credential):
    '''
    function to delete a credential
    '''
    Credential.delete_credential()
def check_existing_credential(account_name):
    '''
    to check if a credential exists
    '''
    return Credential.credential_exists(account_name)
def find_credential(account_name):
    '''
    to find a specific saved credential
    '''
    return Credential.find_by_account_name(account_name)

def main():
    print('**'*15+'PASSWORD-LOCKER'+'**'*15)
    
    name = input('Enter your name: ')
    print(name+' welcome to Password Locker')
    
    print('  '*15+'Create new account'+'  '*15)
    print(name+' type "n" to create a new password locker account ')

    while True:
        response = input().lower()
        
        if response == 'n':
            print('__'*30)
            
            print('Enter your username ')
            username = input()
            
            print(name+' would you like us to generate a password for you?')
            print('''use
                     g-for us to automatically generate a password for you
                     m-for you to manually write your own password
                     ''')
            pref = input().lower()
            print('\n')
            if pref == 'm':
                print('Enter your password: ')
                password = input()
            elif pref == 'g':
                password = password_generetor()
                print(f'Your generated password is{password}')
                break
            else:
                print('Please respond with a valid option either "m" or "g"')
                break
            
            save_user(create_user(username,password))
            break
            
    print(f'User: {username}, Password: {password}')
    print(f'{name} you have successfully created your password locker account') 
    print('__'*30)
            
    print('You can now add,save and view saved accounts and passwords ')   
                
    while True:
            print('''Use:
                 nc - New credential
                 sc - See credential
                 fc - Find credential
              ''')
            choice = input().lower()
            if choice == 'nc':
                print(f'''{name} Reply with "z" to make a password which we can
                  store for you or with "g" and we will generate a random
                  password for you.
                  ''')
                choice_rep = input().lower()
            
                if choice_rep == 'z':
                    print('Enter account name: ')
                    account_name = input()
                    print('Enter account password: ')
                    password = input()
                
                elif choice_rep == 'g':
                    print('Enter account name: ')
                    account_name = input()
                    password = password_generetor()
                    print(f'''{name} your credentials have been stored as
                                  account name: {account_name}
                                  account password: {password}''')
                else:
                    print('Use the options provided please')                
                    save_credential(create_credential(account_name,password))
                    break
                print('Account credentials have been saved succesfully')
                print('__'*30)
    
            elif choice == 'sc':
                credential = new_credential
                if display_credential(credential):
                    print('Here are your saved credentials.')
                    print('\n')
                
                for credential in display_credential():
                    print(f'{Credential.account_name} .....{Credential.account_password}')
                    print('\n')
            
                else:
                    print('\n')
                    print('You dont have any saved credentials as at yet.')
                    print('\n')
                
            elif choice == 'fc':
                print('Enter the username of the account you are searching for: ')
                src = input().title()
                if check_existing_credential(src):
                    search_credential = find_credential(src)
                    print(f'{search_credential.account_name}  {search_credential.account_password}')
                    print('__'*30)
                else:
                    print(f'{name} the account you are looking for is not saved yet.')
                break
            else:
                print('Kindly check your entry and try again.')
            break

    print('**'*30)
                
if __name__ == '__main__':
    main()