'''
Purpose:  get sensor data from AstroPiOTA

Input format:
hash=PNXIVEDHRDHXYHOQVBZFVPSDOWUZTCKBDQRZBKZGYQQWPILDULCQPHCOO9HIGDLNZMFMVGTUJQQTCU999,
tag=ASTROPIOTA99999999999999999,
timestamp=190715 01:50,
pitch=19.930109507503687,
roll=112.40039335928954,
yaw=240.86699355318052,
x=-0.3398926854133606,
y=0.8670123219490051,
z=-0.3559992015361786,
temperature=31.009998321533203,
humidity=36.00428009033203
pressure=1017.124755859375,
device_name=AstroPiOTA,
city=Los Angeles CA USB,
lat=33.893916,
lng=-118.323411

Make sure the output file has a header with these field names:
timestamp,lng,lat,location,temperature,humidity,pressure,gyroY,gyroZ,gyroX,accelX,accelY,accelZ
'''
# set the number of hashes to be downloaded at one time
n = 30

from iota import Iota
from iota import Transaction
import os
import pprint
#api = Iota('https://nodes.devnet.iota.org:443')
api = Iota('https://altnodes.devnet.iota.org')
address = 'VFMEYGUNJVBMRFORVRIOHVET9L9A9AJFCETCOEVI9WPJPRWWALLOBFLXQGGHTZWQKTBJELJNVA9SILXVZTMPMXKPWC'

# Get Trytes accepts multiple Transaction Hashes
transactions = api.find_transactions(addresses=[address])
hashes = []
for txhash in transactions['hashes']:
    hashes.append(txhash)
print(len(hashes), " hashes")

chunks=[]
# Divide the list of hashes into small batches
if len(hashes) > n:
    chunks =[hashes[i:i + n] for i in range(0,len(hashes), n)]
else:
    chunks.append(hashes)
print(len(chunks), " batches")

for chunk in chunks:
    try:
        trytes = api.get_trytes(chunk)['trytes']
    except Exception as e:
        print("EXCEPTION ", e)

    print(len(trytes), " messages")

    msgList = []
    # Get the embedded message from the Signature Message Fragment
    for trytestring in trytes:
        tx = Transaction.from_tryte_string(trytestring)
        message = tx.signature_message_fragment
        msg = {}
        msg['hash'] = str(tx.hash)
        msg['tag'] = str(tx.tag)
        fields = message.decode().split(",")
        for field in fields:
            field = field.split("=")
            try:
                msg[field[0]] = field[1]
            except:
                print(tx.hash, "\n", field)
                continue
        msgList.append(msg)
        
    path='/home/iotahub/data/AstroPiOTA_history.csv'
    if not os.path.exists(path):
        fo = open(path,'a')
        print("timestamp,lng,lat,location,temperature,humidity,pressure,gyroY,gyroZ,gyroX,accelX,accelY,accelZ",file=fo)
    else:
        fo = open(path,'a')

    for m in range(len(msgList)):
        dict = msgList[m]
        #print(dict)
        try:
            print('20{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(dict["timestamp"],dict["lng"],dict["lat"],dict["city"],dict["temperature"],dict["humidity"],dict["pressure"],dict["yaw"],dict["pitch"],dict["roll"],dict["x"],dict["y"],dict["z"],dict["hash"]), file=fo)
        except:
            print(hash, "\n", dict)
    fo.close()

    print("Messages saved in AstroPiOTA_history.csv")
