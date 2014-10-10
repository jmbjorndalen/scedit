#!/usr/bin/env python
#
# apt-get install python-beaker  (req for cork)
# pip install bottle-cork
#
# http://cork.firelet.net/
# 
# 

import bottle
from bottle import request
from cork import Cork

# Use users.json and roles.json in the local example_conf directory
auth = Cork('auth')

#@bottle.route('/login', method='GET')
#def login_form():
#    return '''
#    <form method="POST">
#    <p> Username: <input name="user">
#    <p> Password: <input name="pwd" type="password" value="">
#    <p> <input type="submit" value="Login">
#    </form> 
#    '''

@bottle.route('/login')
@bottle.view('login_form')
def login_form():
    """Serve login form"""
    return {}

def postd():
    return bottle.request.forms

def post_get(name, default=''):
    return bottle.request.POST.get(name, default).strip()

@bottle.post('/login')
def login():
    """Authenticate users"""
    username = post_get('username')
    password = post_get('password')
    auth.login(username, password, success_redirect='/edit/', fail_redirect='/login')

@bottle.route('/logout')
def logout():
    auth.logout(success_redirect='/login')
    

def req_admin():
    auth.require(role='admin', fail_redirect='/sorry_page')


@bottle.route('/admin')
def admin():
    """Only administrators can see this"""
    aaa.require(role='admin', fail_redirect='/sorry_page')
    return 'Welcome administrators'


@bottle.route('/my_role')
def show_current_user_role():
    """Show current user role"""
    session = bottle.request.environ.get('beaker.session')
    print "Session from simple_webapp", repr(session)
    
    auth.require(fail_redirect='/login')
    return auth.current_user.role


@bottle.route('/sorry_page')
def sorry_page():
    """Serve sorry page"""
    return '<p>Sorry, you are not authorized to perform this action</p> <a href="/login">Please login</a>'
