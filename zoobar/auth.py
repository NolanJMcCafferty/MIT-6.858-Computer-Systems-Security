from zoodb import *
from debug import *

import hashlib
import os
import random
import pbkdf2

SALT_LENGTH = 10

def newtoken(cred_db, credentials):
    hashinput = "%s%.10f" % (credentials.password, random.random())
    credentials.token = hashlib.md5(hashinput.encode('utf-8')).hexdigest()
    cred_db.commit()
    return credentials.token

def login(username, password):
    db = person_setup()
    person = db.query(Person).get(username)
    if not person:
        return None
    cred_db = cred_setup()
    credentials = cred_db.query(Cred).get(username)
    
    if pbkdf2.PBKDF2(password, credentials.salt).hexread(32) == credentials.password:
        return newtoken(cred_db, credentials)
    else:
        return None

def register(username, password):
    db = person_setup()
    person = db.query(Person).get(username)
    if person:
        return None
    newperson = Person()
    newperson.username = username
    db.add(newperson)
    db.commit()

    cred_db = cred_setup()
    new_credentials = Cred()
    new_credentials.username = username
    salt = os.urandom(SALT_LENGTH)
    new_credentials.salt = salt
    new_credentials.password = pbkdf2.PBKDF2(password, salt).hexread(32)

    cred_db.add(new_credentials)
    cred_db.commit()
    return newtoken(cred_db, new_credentials)

def check_token(username, token):
    cred_db = cred_setup()
    credentials  = cred_db.query(Cred).get(username)
    if credentials and credentials.token == token:
        return True
    else:
        return False

    
