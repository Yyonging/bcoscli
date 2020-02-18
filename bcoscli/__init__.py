import cod

from .commands import *
from .config import set_config

def main():
    cod.echo('welcome! FICOS-BCOS client for u!')
    cod.main()

getClientVersion = getClientVersion.callback
getGroupList = getGroupList.callback
getBlockByHash = getBlockByHash.callback
getBlockByNumber = getBlockByNumber.callback
getBlockHashByNumber = getBlockHashByNumber.callback
getTransactionByHash = getTransactionByHash.callback
getTransactionByBlockHashAndIndex = getTransactionByBlockHashAndIndex.callback
getTransactionByBlockNumberAndIndex = getTransactionByBlockNumberAndIndex.callback
getTransactionReceipt = getTransactionReceipt.callback
getCode = getCode.callback
getSystemConfigByKey = getSystemConfigByKey.callback
call = call.callback
sendRawTransaction = sendRawTransaction.callback
getTransactionByHashWithProof = getTransactionByHashWithProof.callback
getTransactionReceiptByHashWithProof = getTransactionReceiptByHashWithProof.callback
