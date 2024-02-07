#!/usr/bin/env python3

import rpclib
import sys
import auth
from debug import *
import bank

class BankRpcServer(rpclib.RpcServer):
    def rpc_transfer(self, sender, sender_token, recipient, zoobars):
        return bank.transfer(sender, sender_token, recipient, zoobars, self.caller == "profile")

    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_initialize(self, username):
        return bank.initialize(username)

    def rpc_get_log(self, username):
        return bank.get_log(username)

if len(sys.argv) != 2:
    print(sys.argv[0], "too few args")

s = BankRpcServer()
s.run_fork(sys.argv[1])
