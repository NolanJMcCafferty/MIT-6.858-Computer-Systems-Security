from zoodb import *
from debug import *

import auth_client
import time

INITIAL_ZOOBARS = 10

def transfer(sender, sender_token, recipient, zoobars, is_profile):
    persondb = person_setup()
    senderp = persondb.query(Person).get(sender)
    recipientp = persondb.query(Person).get(recipient)

    bankdb = bank_setup()
    senderbank = bankdb.query(Bank).get(sender)
    sender_balance = senderbank.zoobars - zoobars

    recipientbank = bankdb.query(Bank).get(recipient)
    recipient_balance = recipientbank.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()
   
    if not is_profile and not auth_client.check_token(sender, sender_token):
        raise Exception

    senderbank.zoobars = sender_balance
    
    recipientbank.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def initialize(username):
    db = bank_setup()
    newbank = Bank()
    newbank.username = username
    newbank.zoobars = INITIAL_ZOOBARS
    db.add(newbank)
    db.commit()

def balance(username):
    db = bank_setup()
    user = db.query(Bank).get(username)
    return user.zoobars

def get_log(username):
    db = transfer_setup()
    l = db.query(Transfer).filter(or_(Transfer.sender==username,
                                      Transfer.recipient==username))
    r = []
    for t in l:
       r.append({'time': t.time,
                 'sender': t.sender ,
                 'recipient': t.recipient,
                 'amount': t.amount })
    return r 


