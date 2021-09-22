import datetime as datatime
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import streamlit as st
# import matplotlib.pyplot as plt
# import matplotlib.style

# matplotlib.style.use('ggplt')

start = '2021-09-01'
end   = '2021-10-30'

_nikkei = pdr.DataReader('^NKX','stooq',start,end)
nikkei = pd.DataFrame(_nikkei.iloc[:,3])
nikkei.columns = ['^NKX',]
nikkei_change = nikkei.pct_change()

st.title('日経平均')
st.write(nikkei_change)
st.line_chart(nikkei_change)


# stooq = StooqDailyReader(brand, start=start, end=end)
# data = stooq.read()  # pandas.core.frame.DataFrame
# print(data)
