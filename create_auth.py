#!/usr/bin/env python
#
#
# Regenerate files in example_conf

from datetime import datetime
from cork import Cork

def makeuser(cork, username, password, tstamp):
    cork._store.users[username] = {
        'role': 'admin',
        'hash': cork._hash(username, password),
        'email_addr': username + '@localhost.local',
        'desc': username + ' test user',
        'creation_date': tstamp
    }
    



def populate_conf_directory():
    cork = Cork('auth', initialize=True)

    cork._store.roles['admin'] = 100
    cork._store.roles['editor'] = 60
    cork._store.roles['user'] = 50
    cork._store._savejson('roles', cork._store.roles)

    tstamp = str(datetime.utcnow())
    print "Change the usernames and passwords in the code"
    exit()
    makeuser(cork, 'admin', 'CHANGEME', tstamp)
    makeuser(cork, 'someuser', 'CHANGEME', tstamp)
    makeuser(cork, 'woohoo', 'CHANGEME', tstamp)
    
    cork._store._save_users()

if __name__ == '__main__':
    populate_conf_directory()
    
