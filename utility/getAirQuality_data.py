'''
Purpose:  get sensor data from AirQuality

make sure the output file has this header:
TIMESTAMP,LNG,LAT,CO2_PPM,TVOC_PPB

'''
# batch size
n=30

from iota import Iota
from iota import Transaction
import os

import pprint
#api = Iota('https://nodes.devnet.iota.org:443')
api = Iota('https://altnodes.devnet.iota.org')
address = 'K9LYCBRIBMKPDPMDPTJSQTCXYVPBULSIRQZJEHINYQXBYNFCFSWUXIMXELKTGXCZLYDZNDJEVKSOBWDXXTTNMMPRPC'

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
    print(len(trytes), " messages/batch")
    k+= len(trytes)
    print(k, " messages saved")

    msgList = []
    # Get the embedded message from the Signature Message Fragment
    for trytestring in trytes:
        tx = Transaction.from_tryte_string(trytestring)
        message = tx.signature_message_fragment
        msg = {}
        msg['hash'] = str(tx.hash)
        msg['tag'] = str(tx.tag)
        fields = message.decode().split(",")
        for f in range(len(fields)):
            fields[f] = fields[f].strip("\n")
            msg["co2-ppm"] = fields[0]
            msg["tvoc-ppb"] = fields[1]
            msg["timestamp"] = fields[2]
        msgList.append(msg)

    path = '/home/iotahub/data/AirQuality_history.csv'
    if not os.path.exists(path):
        fo = open(path,'a')
        print("TIMESTAMP,LNG,LAT,CO2_PPM,TVOC_PPB",file=fo)
    else:
        fo = open(path,'a')

    for m in range(len(msgList)):
        dict = msgList[m]
        try:
            print('{},{},{},{},{}'.format(dict["timestamp"],"-118.323","33.893",dict["co2-ppm"],dict["tvoc-ppb"]), file=fo)
        except:
            print("DICT EXCEPTION ", hash, "\n", dict)
    fo.close()

    print("Messages saved in AirQuality_history.csv")
