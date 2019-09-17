'''
Purpose:  get sensor data from Envirophat

'''
#batch size
n=30

from iota import Iota
from iota import Transaction
import os
import pprint
#api = Iota('https://nodes.devnet.iota.org:443')
api = Iota('https://altnodes.devnet.iota.org')
address = 'ORTP9BWTENDHERKNXRHRN9CAYPWSUXDPUZGFJVV9APCWORUFSE9N9OQYBSJEQAIBHJSWBIGFNQUDT9IUWBBPUYLAHB'

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
    try:
        trytes = api.get_trytes(chunk)['trytes']
        print(len(trytes), " messages")
    except Exception as e:
        print("CHUNK EXCEPTION ", e)
        continue

    k+= len(trytes)
    print(k, " messages saved")

    msgList = []
    # Get the embedded message from the Signature Message Fragment
    for trytestring in trytes:
        try:
            tx = Transaction.from_tryte_string(trytestring)
        except Exception as e:
            print("TRYTESTRING EXCEPTION ", e)
            continue
        message = tx.signature_message_fragment
        msg = {}
        msg['hash'] = str(tx.hash)
        msg['tag'] = str(tx.tag)
        fields = message.decode().split(",")
        for f in range(len(fields)):
            msg["lux"] = fields[0]
            msg["rgb"] = fields[1]
            msg["accelX"] = fields[2]
            msg["accelY"] = fields[3]
            msg["accelZ"] = fields[4]
            msg["heading"] = fields[5]
            msg["temp"] = fields[6]
            msg["press"] = fields[7]
            msg["location"] = fields[8]
            msg["timestamp"] = fields[9]
        msgList.append(msg)

    path='/home/iotahub/data/Envirophat_history.csv'
    if not os.path.exists(path):
        fo = open(path,'a')
	print("timestamp,lng,lat,location,temperature,humidity,pressure,yaw,pitch,roll,accelX,accelY,accelZ,heading,rgb,hash",file=fo)
    else:
        fo = open(path,'a')

    for m in range(len(msgList)):
        dict = msgList[m]
        try:
		print('20{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(dict["timestamp"],dict["lng"],dict["lat"],dict["city"],dict["temperature"],dict["humidity"],dict["pressure"],dict["yaw"],dict["pitch"],dict["roll"],dict["x"],dict["y"],dict["z"],dict["hash"]), file=fo)
        except:
            	print("DICT EXCEPTION:", hash, "\n", dict)
    fo.close()

    print("Messages saved in Envirophat_history.csv")
