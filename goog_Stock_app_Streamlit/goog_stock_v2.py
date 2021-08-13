from pandas_datareader import data as pdr
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from PIL import Image
import yfinance as yf
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import pandas as pd



yf.pdr_override()

st.title("Google stock report")

st.header("Last 8 months to till date")


data_google = pdr.get_data_yahoo("GOOG", start="2021-01-01", end="2021-08-13")

st.dataframe(data_google)


fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=data_google, x="Date", y="Close")
ax.set_title(" Google(Ticker:GOOG): Stock Prices Closing - 2021-01 to 2021-08 ")
st.pyplot(fig)


finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'FB']

# Parsing html tables

news_tables = {}
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)

    html = BeautifulSoup(response, features='html.parser')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table

parsed_data = []

for ticker, news_table in news_tables.items():

    for row in news_table.findAll('tr'):

        title = row.a.text
        date_data = row.td.text.split(' ')

        if len(date_data) == 1:
            time = date_data[0]
        else:
            date = date_data[0]
            time = date_data[1]

        parsed_data.append([ticker, date, time, title])

df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

nltk.download('vader_lexicon')

vader = SentimentIntensityAnalyzer()

f = lambda title: vader.polarity_scores(title)['compound']
df['compound'] = df['title'].apply(f)
df['date'] = pd.to_datetime(df.date).dt.date
df_goog_sentiment = df.loc[df['ticker'] == 'GOOG']


st.dataframe(df_goog_sentiment)

plt.figure(figsize=(20,15))      # figure size
# unstack() allows us to have dates as x-axis
mean_df = df_goog_sentiment.groupby(['date', 'ticker']).mean() # avg compund score for each date
mean_df = mean_df.unstack() 
# xs (cross section of compund) get rids of compund label
mean_df = mean_df.xs('compound', axis="columns")
mean_df.plot(kind='bar')
plt.savefig('fig1.png')

image = Image.open('fig1.png')

st.image(image, caption='Polarity scores for GOOG')


