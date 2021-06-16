import datetime as datatime

import numpy as np
import pandas as pd
import pandas_datareader as pdr
import streamlit as st

brand = '6857.JP'
test = pdr.DataReader(brand,'stooq','2021-06-01','2021-06-30')

dftest = pd.DataFrame(test) 
dftest.head

st.title('株価データ')
st.write(dftest)


# stooq = StooqDailyReader(brand, start=start, end=end)
# data = stooq.read()  # pandas.core.frame.DataFrame
# print(data)
