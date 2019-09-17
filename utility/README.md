# Retrieving sensor data from Tangle test addresses

**Storing data at one address on the Tangle is not secure but it is useful when prototyping or learning.  This utility script downloads data stored in one address in small chunks.**

### AutoGardener
Set the chunk size.  In this example, the script gets sensor data from AutoGardener in chunks of 30 hashes
```
n=30
```
Import the Iota client libraries
```
from iota import Iota
from iota import Transaction
```
Import the operating system library
```
import os
```
Import the pretty print library
```
import pprint
```
Set the api to the Iota testbed called, Devnet
```
api = Iota('https://nodes.devnet.iota.org:443')
```
Set the address
```
address = 'ZNJWDJBGQVLCNJIRXPDUKHESBYXGFADCKAUCXFZFCWEOUJOJIDZHDCMVQQTEMZIMPOXFCTM9QSNNUZVBXMHVKFPSF9'
```
Get the hashes for all the transactions located at the address
```
transactions = api.find_transactions(addresses=[address])
hashes = []
for txhash in transactions['hashes']:
    hashes.append(txhash)
```
Get the total number of hashes
```
print(len(hashes), " hashes")
```
Divide the total number of hashes by the chuck size
```
chunks = []
if len(hashes) > n:
    chunks =[hashes[i:i + n] for i in range(0,len(hashes), n)]
else:
    chunks.append(hashes)
print(len(chunks), " batches")
```
Get the sensor data for each hash in the chunck
```
k=0
for chunk in chunks:
    trytes = api.get_trytes(chunk)['trytes']
    print(len(trytes), " messages")
    k+= len(trytes)
    print(k, " messages saved")
```
Decipher the message in each transaction
```
    msgList = []
        for trytestring in trytes:
        tx = Transaction.from_tryte_string(trytestring)
        message = tx.signature_message_fragment
        msg = {}
        msg['hash'] = str(tx.hash)
        fields = message.decode().split(",")
        for f in range(len(fields)):
            msg["status"] = fields[f].strip("\n")
        msgList.append(msg)
```
Set the path to the CSV file where the data will be stored
```
    path = '/home/iotahub/data/AutoGardener_history.csv'
```
Print the field names on the first row of the CSV file.  The field names for AutoGardener are longitude, latitude, watering status, and the hash
```
    if not os.path.exists(path):
        fo = open(path,'a')
        # CSV HEADER
        print("LNG,LAT,STATUS,HASH",file=fo)   
    else:
        fo = open(path,'a')
```
Store the data from each transaction in the CSV file
```
    for m in range(len(msgList)):
        dict = msgList[m]
        try:
            # CSV ROW
            print('{},{},{},{}'.format("-118.323","33.893",dict["status"],dict["hash"]), file=fo)   
        except:
            print("DICT EXCEPTION ", hash, "\n", dict)
    fo.close()
```
Print a message when all the messages have been saved
```
    print("Messages saved in AutoGardener_history.csv")
```

[Complete Script for Autonomous Gardener](getAutoGardener_data.py)

In order to customize this script for other IoT Devices, change three lines of code.

### AstroPiOTA

Change the address
```
address = 'VFMEYGUNJVBMRFORVRIOHVET9L9A9AJFCETCOEVI9WPJPRWWALLOBFLXQGGHTZWQKTBJELJNVA9SILXVZTMPMXKPWC'

```
Change the CSV HEADER
```
        print("timestamp,lng,lat,location,temperature,humidity,pressure,gyroY,gyroZ,gyroX,accelX,accelY,accelZ",file=fo)

```
Change the CSV ROW
```
print('20{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(dict["timestamp"],dict["lng"],dict["lat"],dict["city"],dict["temperature"],dict["humidity"],dict["pressure"],dict["yaw"],dict["pitch"],dict["roll"],dict["x"],dict["y"],dict["z"],dict["hash"]), file=fo)
```
[Complete Script for AstroPiOTA](getAstroPiOTA_data.py)


### Envirophat
Change the address
```
address = 'ORTP9BWTENDHERKNXRHRN9CAYPWSUXDPUZGFJVV9APCWORUFSE9N9OQYBSJEQAIBHJSWBIGFNQUDT9IUWBBPUYLAHB'

```
Change the CSV HEADER
```
print("timestamp,lng,lat,location,temperature,humidity,pressure,yaw,pitch,roll,accelX,accelY,accelZ,heading,rgb,hash",file=fo)
```
Change the CSV ROW
```
print('{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(dict["timestamp"],"-118.323","33.893",dict["location"],dict["temp"],0,dict["press"],0,0,0,dict["accelX"],dict["accelY"],dict["accelZ"],dict["heading"],dict["rgb"]), file=fo)
```
[Complete Script for EnviroPhat](getEnvirophat_data.py)


### CO2-TVOC
Change the address
```
address = 'K9LYCBRIBMKPDPMDPTJSQTCXYVPBULSIRQZJEHINYQXBYNFCFSWUXIMXELKTGXCZLYDZNDJEVKSOBWDXXTTNMMPRPC'

```
Change the CSV HEADER
```
print("TIMESTAMP,LNG,LAT,CO2_PPM,TVOC_PPB",file=fo)
```
Change the CSV ROW
```
print('{},{},{},{},{}'.format(dict["timestamp"],"-118.323","33.893",dict["co2-ppm"],dict["tvoc-ppb"]), file=fo)
```
[Complete Script for CO2-TVOC](getCO2-TVOC_data.py)
