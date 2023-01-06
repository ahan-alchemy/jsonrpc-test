import requests
from time import sleep
from threading import Thread


STG_ETH_URL = 'https://eth-mainnet.g.alchemypreview.com/v2/{}'.format("li8QvtUVaM2e4_pljgPoU6NeXWAw-iRU")
PROD_ETH_URL = 'https://eth-mainnet.g.alchemy.com/v2/{}'.format("Ko-nQxxHOBt7OE7JpmcLld7b-3Eg3uVS")


def json_rpc(method, params=[], do_print=False):
    headers = {'Content-Type': 'application/json'}
    data = {'ahan': 'testing', 'method': method, 'params': params, 'id': 1, 'jsonrpc': '2.0'}
    res = requests.post(PROD_ETH_URL, headers=headers, json=data, timeout=10)
    if do_print:
        print(res.json())
    return res.json()


def hex_to_dec(hex):
    return int(hex, 16)


def dec_to_hex(dec):
    return hex(dec)

def countup():
    while True:
        resp = json_rpc('eth_blockNumber')
        block_num = resp['result']
        block = json_rpc('eth_getBlockByNumber', [block_num, False])
        hash = block['result']['hash']
        print('countup hash %s' % hash)
        json_rpc('eth_getUncleCountByBlockHash', [hash], True)
        sleep(10)

def countdown(start_num):
    for block_number in range(start_num, -1, -1):
        block = json_rpc('eth_getBlockByNumber', [str(dec_to_hex(block_number)), False])
        hash = block['result']['hash']
        print('countdown hash %s' % hash)
        json_rpc('eth_getUncleCountByBlockHash', [hash], True)
        sleep(2)


if __name__ == '__main__':
    Thread(target=countup).start()
    Thread(target=countdown, args=(15537385,)).start()
