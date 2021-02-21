#!/usr/bin/env python3.6
from user import User

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
def find_user(username)
    '''
    Function that finds a user by username and returns 
    the user
    '''
    return User.find_by_username(username)
def check_existing_users(username):
    '''
    Function that check if a user exists with that username
    '''
    return user.user_exist(username)




print('**'*15+'PASSWORD-LOCKER'+'**'*15)
