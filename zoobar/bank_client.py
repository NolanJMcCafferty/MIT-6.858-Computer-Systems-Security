from debug import *
from zoodb import *
import rpclib

sys.path.append(os.getcwd())
import readconf

def transfer(sender, recipient, zoobars, sender_token):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('transfer', sender=sender, sender_token=sender_token, recipient=recipient, zoobars=zoobars)
        return ret

def balance(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('balance', username=username)
        return ret

def initialize(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('initialize', username=username)
        return ret

def get_log(username):
    host = readconf.read_conf().lookup_host('bank')
    with rpclib.client_connect(host) as c:
        ret = c.call('get_log', username=username)
        return ret
