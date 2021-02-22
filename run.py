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
                
                
                
                
                
if __name__ == '__main__':
    main()