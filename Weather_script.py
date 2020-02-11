# -*- coding: utf-8 -*-

##### Import os module to enable python to read directory.
#### Use exception handling in case user has not got os module installed in the machine.
try:
    import os
except ImportError:
    os.system("pip install os")
    import os

try:
    import numpy as np
except ImportError:
    os.system("pip install numpy")



#### Import pandas module. Use 'pip install pandas' to install the module.
#### Use exception handling in case user has not got pandas installed in the machine.
try:
    import pandas as pd
except ImportError:
    os.system("pip install pandas")
    import pandas as pd

#### Import pyarrow module in order to read/save parquet files. Use 'pip install pyarrow' to install the module.
#### Use exception handling in case user has not got pyarrow installed in the machine.
try:
    import pyarrow
except ImportError:
    os.system("pip install pyarrow")
    import pyarrow

from pyarrow import parquet as pq


#### Name of the file.
FILE = "weather.20160201.csv"
FILE2 = "weather.20160301.csv"

#### Read the csv file into DataFrame in python.
DATA = pd.read_csv(FILE)
DATA2 = pd.read_csv(FILE2)

#### Combine two datasets into one as we're interested in the max temperature as a whole.
DATA = pd.concat([DATA,DATA2])

#### Save the first data to parquet file.
DATA.to_parquet('DATA.parquet')

#### Read parquet file
Data_pq = pq.read_table('DATA.parquet')
#### Convert it to a pandas DataFrame
Data_pq = Data_pq.to_pandas()

#### -99 is assumed to be a missing value, so therefore query data to remove these values from the data.
Data_pq = Data_pq[Data_pq['ScreenTemperature'] > -99]

#### Find the row with the max temperature.
Data_pq_max_temp = Data_pq[Data_pq['ScreenTemperature'] == Data_pq['ScreenTemperature'].max()]

#### Focus on hottest date, temperature of the hottest day, and region.
Data_pq_max_temp = Data_pq_max_temp[['ObservationDate','ScreenTemperature','Region']]

#### Print out Date/time of the max temperature, max temperature and region of the max temperature.
Date_time = Data_pq_max_temp['ObservationDate'].to_excel("Date of hottest day.xlsx")
Temperature = Data_pq_max_temp['ScreenTemperature'].to_excel("Hottest temperature.xlsx")
Region = Data_pq_max_temp['Region'].to_excel("Region of hottest temperature.xlsx")

#### For unit testing
Date_time_str = Data_pq_max_temp['ObservationDate'][Data_pq_max_temp.index[0]]
Temperature_value = Data_pq_max_temp['ScreenTemperature'][Data_pq_max_temp.index[0]]
Region_str = Data_pq_max_temp['Region'][Data_pq_max_temp.index[0]]

print("The date of the hottest day is "+ Date_time_str)
print("The hottest temperature is " + str(Temperature_value))
print("The region of the hottest temperature is " + Region_str)


