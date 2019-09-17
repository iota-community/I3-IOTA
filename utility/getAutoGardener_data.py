'''
Purpose:  get sensor data from AutoGardener

'''
#batch size
n=30

from iota import Iota
from iota import Transaction
import os

import pprint
#api = Iota('https://nodes.devnet.iota.org:443')
api = Iota('https://altnodes.devnet.iota.org')
address = 'ZNJWDJBGQVLCNJIRXPDUKHESBYXGFADCKAUCXFZFCWEOUJOJIDZHDCMVQQTEMZIMPOXFCTM9QSNNUZVBXMHVKFPSF9'

# Get Trytes accepts multiple Transaction Hashes
transactions = api.find_transactions(addresses=[address])
hashes = []
for txhash in transactions['hashes']:
    hashes.append(txhash)
print(len(hashes), " hashes")

# Divide the list of hashes into small batches
chunks = []
if len(hashes) > n:
    chunks =[hashes[i:i + n] for i in range(0,len(hashes), n)]
else:
    chunks.append(hashes)
print(len(chunks), " batches")

k=0
for chunk in chunks:
    trytes = api.get_trytes(chunk)['trytes']
    print(len(trytes), " messages")
    k+= len(trytes)
    print(k, " messages saved")

    msgList = []
    # Get the embedded message from the Signature Message Fragment
    for trytestring in trytes:
        tx = Transaction.from_tryte_string(trytestring)
        message = tx.signature_message_fragment
        msg = {}
        msg['hash'] = str(tx.hash)
        fields = message.decode().split(",")
        for f in range(len(fields)):
            msg["status"] = fields[f].strip("\n")
        msgList.append(msg)

    path = '/home/iotahub/data/AutoGardener_history.csv'
    if not os.path.exists(path):
        fo = open(path,'a')
        print("LNG,LAT,STATUS,HASH",file=fo)
    else:
        fo = open(path,'a')

    for m in range(len(msgList)):
        dict = msgList[m]
        try:
            print('{},{},{},{}'.format("-118.323","33.893",dict["status"],dict["hash"]), file=fo)
        except:
            print("DICT EXCEPTION ", hash, "\n", dict)
    fo.close()

    print("Messages saved in AutoGardener_history.csv")
