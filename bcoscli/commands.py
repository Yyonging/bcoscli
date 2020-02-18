import requests
import json
import click

from .config import Config
from cod import echo
from types import FunctionType

s = requests.Session()

def decode_res(res):
    try:
        text = json.loads(res.text)
        if Config.ECHO:
            echo(json.dumps(text, indent=4))
        return text
    except json.decoder.JSONDecodeError as excep:
        echo(excep)

group_commands = ["getBlockNumber", "getPbftView", "getSealerList", "getObserverList",
    "getConsensusStatus", "getSyncStatus", "getPeers", "getGroupPeers", "getNodeIDList",
    "getPendingTransactions", "getPendingTxSize", "getTotalTransactionCount"]

for c_name in group_commands:
    template_func_code = f'''def template_func(gid):
        data = {{"jsonrpc":"2.0","method":"{c_name}","params":[int(gid)],"id":1}}
        res = s.post(Config.HOST_RPC, json=data)
        return decode_res(res)
    '''
    template = compile(template_func_code, "<string>", "exec")
    template_func = FunctionType(template.co_consts[0], globals(), c_name)
    globals()[c_name] = template_func
    click.command()(click.option('--gid', prompt='group id')(template_func))

@click.command()
def getClientVersion():
    data = {"jsonrpc":"2.0","method":"getClientVersion","params":[],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
def getGroupList():
    data = {"jsonrpc":"2.0","method":"getGroupList","params":[],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--block_hash', prompt='blockHash')
@click.option('--is_include_transactions', prompt='is include transactions, true or false')
def getBlockByHash(gid, block_hash, is_include_transactions):
    data = {"jsonrpc":"2.0","method":"getBlockByHash","params":[int(gid), block_hash, is_include_transactions],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--block_hash', prompt='blockHash')
@click.option('--is_include_transactions', prompt='is include transactions, true or false')
def getBlockByNumber(gid, block_hash, is_include_transactions):
    data = {"jsonrpc":"2.0","method":"getBlockByNumber","params":[int(gid), block_hash, is_include_transactions],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)


@click.command()
@click.option('--gid', prompt='group id')
@click.option('--block_num', prompt='block number')
def getBlockHashByNumber(gid, block_num):
    data = {"jsonrpc":"2.0","method":"getBlockHashByNumber","params":[int(gid), block_num],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--transaction_hash', prompt='block number')
def getTransactionByHash(gid, transaction_hash):
    data = {"jsonrpc":"2.0","method":"getTransactionByHash","params":[int(gid), transaction_hash],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--block_hash', prompt='block hash')
@click.option('--transaction_index', prompt='transaction index')
def getTransactionByBlockHashAndIndex(gid, block_hash, transaction_index):
    data = {"jsonrpc":"2.0","method":"getTransactionByBlockHashAndIndex",
        "params":[int(gid), block_hash, transaction_index],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--block_num', prompt='block numbber')
@click.option('--transaction_index', prompt='transaction index')
def getTransactionByBlockNumberAndIndex(gid, block_num, transaction_index):
    data = {"jsonrpc":"2.0","method":"getTransactionByBlockNumberAndIndex",
        "params":[int(gid), block_num, transaction_index],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--transaction_hash', prompt='transaction hash')
def getTransactionReceipt(gid, transaction_hash):
    data = {"jsonrpc":"2.0","method":"getTransactionReceipt",
        "params":[int(gid), transaction_hash],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--address', prompt='address')
def getCode(gid, address):
    data = {"jsonrpc":"2.0","method":"getCode","params":[int(gid), address],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--key', prompt='key name, tx_count_limit or tx_gas_limit')
def getSystemConfigByKey(gid, key):
    data = {"jsonrpc":"2.0","method":"getSystemConfigByKey","params":[int(gid), key],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--from_address', prompt='send address')
@click.option('--to_address', prompt='target address')
@click.option('--value', prompt='optional value')
@click.option('--d', prompt='optional data')
def call(gid, key, from_address, to_address, value, d):
    data = {"jsonrpc":"2.0","method":"call",
        "params":[int(gid), {"from":from_address, "to":to_address, "value":value, "data":d}],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--rlp', prompt='signed transaction data')
def sendRawTransaction(gid, rlp):
    data = {"jsonrpc":"2.0","method":"sendRawTransaction",
        "params":[int(gid), rlp],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--transaction_hash', prompt='transaction hash')
def getTransactionByHashWithProof(gid, transaction_hash):
    data = {"jsonrpc":"2.0","method":"sendRawTransaction",
        "params":[int(gid), transaction_hash],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

@click.command()
@click.option('--gid', prompt='group id')
@click.option('--transaction_hash', prompt='transaction hash')
def getTransactionReceiptByHashWithProof(gid, transaction_hash):
    data = {"jsonrpc":"2.0","method":"sendRawTransaction",
        "params":[int(gid), transaction_hash],"id":1}
    res = s.post(Config.HOST_RPC, json=data)
    return decode_res(res)

