from transformers import ethereum
import csv


def new_collection(transactions, kind):
    """
    :param transactions: transactions list
    :param kind: incoming or outgoing transactions type (from, to)
    :return: result tree
    """
    tree = []
    if kind == 'from':
        kind = 'to'
    else:
        kind = 'from'
    for tx in transactions:
        if tx[kind] not in tree:
            tree.append(tx[kind])
    return tree


def get_data(address, kind, depth):
    """
    :param address: blockchain address of which transaction raw_data we want to extract
    :param kind: incoming or outgoing transactions
    :param depth: in a breadth-first manner, how many levels to query for raw_data
    :return: full tree of raw_data
    """
    steps, tree, clones = 1, [], [address.lower()]
    initial_query = ethereum.get_transactions(address, kind)
    if depth == 1:
        return initial_query

    full_tree = transactions = initial_query
    while steps < depth:
        tree = new_collection(transactions, kind)
        transactions = []
        for account in tree:
            if account not in clones:
                try:
                    new_transactions = ethereum.get_transactions(account, kind)
                except Exception:
                    continue
                full_tree = full_tree + new_transactions
                transactions = transactions + new_transactions
                clones.append(account)
        steps += 1

    """
    Uncomment this code to remove duplicates if there are no features and then run dfs.py for the output csv
    
    seen = set()  
    new_l = []
    for d in full_tree:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)  
    full_tree = new_l
    """

    return full_tree


address1 = '0x2B0C8440c53edF28b4DA14815b3DdcEf85A6A67f'
address2 = '0xcbe5142afccefb0bc8411eff17513f6d1525fc8c'
address3 = '0x374EC3888a440aD3290ECF61871837f87ef80361'
address4 = '0x027beefcbad782faf69fad12dee97ed894c68549'
address5 = '0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8'
address6 = '0x4f234e804d32aac6d802e0942da77ba0a044ee91'
address7 = '0x5990edaf58b3e758c0e0d8ed63adf9ee26c44a5d'

result_tree = get_data(address1, 'from', 2)

with open('raw_data/graph9.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, fieldnames=result_tree[0].keys())
    fc.writeheader()
    fc.writerows(result_tree)
