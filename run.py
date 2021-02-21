#!/usr/bin/env python3.6
from user import User

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

print('**'*15+'PASSWORD-LOCKER'+'**'*15)
