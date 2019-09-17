# IoT Device Data

The data folder contains csv files with sensor data from the AstroPiOTA environment sensor and the CO2-TVOC air quality sensor

### AstroPiOTA schema

|Field|Description|
|------------|-------------------------------------|
|TIMESTAMP| time of sensor reading|
|LNG| longitude|
|LAT| latitude|
|DEVICE_NAME| AstroPiOTA|
|TEMPERATURE| temperature in degrees Celsius|
|HUMIDITY| percent of humidity|
|PRESSURE| pressure|
|PITCH| vertical position of the gyroscope|
|ROLL|  position of the gyroscope along the z-axis|
|YAW| horizontal position of the gyroscope|
|X| horizontal acceleration|
|Y| vertical acceleration|
|Z| rolling acceleration|

#### CSV File
[August-September 2019](Data_AstroPiOTA-Aug-Sep2019.csv)


### CO2-TVOC schema

|Field|Description|
|-----|------------------------|
|CO2| PPM (parts per million)|
|TVOC| PPB (parts per billion)|
|TIMESTAMP| time of sensor reading|

#### CSV File
[July - September 2019](airquality-Jul-Sep2019.csv)
