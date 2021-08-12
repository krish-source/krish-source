from pandas_datareader import data as pdr
import yfinance as yf
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



yf.pdr_override()

st.title("Google stock report")

st.header("Last 8 months to till date")


data_google = pdr.get_data_yahoo("GOOG", start="2021-01-01", end="2021-08-12")

st.dataframe(data_google)


fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=data_google, x="Date", y="Close")
ax.set_title(" Google(Ticker:GOOG): Stock Prices Closing - 2021-01 to 2021-08 ")
st.pyplot(fig)



