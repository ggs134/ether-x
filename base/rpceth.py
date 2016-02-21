import requests
import json

def getBalance(address):
    addr=str(address)
    data={"jsonrpc": "2.0", "method": "eth_getBalance", "params":[addr, 'latest'], "id":1}
    r = requests.post('http://127.0.0.1:8545', data=json.dumps(data))
    res = json.loads(r.text)
    return int(res['result'],16)

def newAccount(password):
    data ={"jsonrpc": "2.0", "method": "personal_newAccount", "params":[password], "id":1}
    r = requests.post('http://127.0.0.1:8545', data=json.dumps(data))
    res = json.loads(r.text)
    return res['result']