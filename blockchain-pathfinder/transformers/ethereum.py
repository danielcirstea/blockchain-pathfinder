import requests
import certifi
from datetime import datetime
from web3 import Web3

web3 = Web3(Web3.IPCProvider())


def get_time(time_stamp):
    return datetime.utcfromtimestamp(int(time_stamp)).strftime('%Y.%m.%d, %H:%M:%S')


def get_value(value):
    return float(web3.fromWei(float(value), 'ether'))


def get_transactions(address, kind):
    """
    :param address: ethereum blockchain account hash
    :param kind: the kind of transactions: incoming or outgoing (to, from)
    :return: list of transactions made by the input_data address
    """
    tmp_tx = []
    url = 'https://api.etherscan.io/api?module=account&action=txlist&address=' + address.lower() + \
          '&startblock=0&endblock=99999999&sort=asc'
    response = requests.get(url, verify=certifi.where())
    address_content = response.json()
    result = address_content.get('result')
    for transaction in result:
        if transaction.get(kind) == address.lower():
            if transaction.get('txreceipt_status') != '0' and transaction.get('isError') == '0':
                tmp_tx.append({'from': transaction.get('from'), 'to': transaction.get('to')})
    return tmp_tx


"""
 Use this  code to extract timestamp and/or value !

 tmp_tx.append({'from': transaction.get('from'), 'to': transaction.get('to'),
   'value': get_value(transaction.get('value')),
   'timestamp': get_time(transaction.get('timeStamp'))}) 
   
"""



