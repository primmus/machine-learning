#!/usr/bin/python

'''

This script provides the required interface by 'flask-login':

- https://flask-login.readthedocs.io/en/0.4.0/#your-user-class

'''


class User(object):
    '''

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, username):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.username = username

        @property
        def is_authenticated(self):
            '''

            This property should return True if the user is authenticated,
            i.e. they have provided valid credentials. (Only authenticated
            users will fulfill the criteria of login_required.)

            '''

            return self.authenticated
 
        @property
        def is_active(self):
            '''

            This property should return True if this is an active user - in
            addition to being authenticated, they also have activated their
            account, not been suspended, or any condition your application has
            for rejecting an account. Inactive accounts may not log in (without
            being forced of course).

            '''

            return True
 
        @property
        def is_anonymous(self):
            '''

            This property should return True if this is an anonymous user.
            (Actual users should return False instead.)

            '''

            return False

        def get_id(self):
            '''

            This method must return a unicode that uniquely identifies this
            user, and can be used to load the user from the user_loader
            callback. Note that this must be a unicode - if the ID is natively
            an int or some other type, you will need to convert it to unicode.

            '''

            return str(self.uid)