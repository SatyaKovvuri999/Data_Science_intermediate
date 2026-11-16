import streamlit as st
import yfinance as yf
import datetime as dt

st.title("Stock Price Analyser")
st.subheader("This application helps you to analyse the stock price of a company")

ticker = yf.Ticker("MSFT") # AAPL, GOOG, AMZN, TSLA

ticker_data=ticker.history(period="1mo") # 1y, 5d, 1mo, 3mo, 6mo, ytd, max

st.line_chart(ticker_data.Close)

st.write(ticker_data)

st.subheader("Price Movement")
st.line_chart(ticker_data["Close"])

st.subheader("Volumne Movement")
st.bar_chart(ticker_data["Close"])


#with input
symbol = st.text_input(
    "Enter a stock ticker",
    value="MSFT"
)

ticker = yf.Ticker(symbol)

ticker_data=ticker.history(period="1mo") # 1y, 5d, 1mo, 3mo, 6mo, ytd, max

st.write(ticker_data)


#With date
symbol1 = st.text_input(
    "Enter a stock ticker ",
    value="MSFT"
)

ticker = yf.Ticker(symbol1)

start_date = st.date_input(
    "Start date",
    dt.date.today() - dt.timedelta(days=30)
)

end_date = st.date_input(
    "End date",
    dt.date.today()
)

ticker_data=ticker.history(
    start=start_date,
    end=end_date
)

st.write(ticker_data)


#Space adjustment
col1,col2,col3=st.columns(3)
with col1:
    symbol1 = st.text_input(
        "Enter a stock ticker2",
        value="MSFT"
    )

ticker = yf.Ticker(symbol1)

with col2:
    start_date = st.date_input(
        "Start date2",
        dt.date.today() - dt.timedelta(days=30)
    )

with col3:
    end_date = st.date_input(
        "End date2",
        dt.date.today()
    )

ticker_data=ticker.history(
    start=start_date,
    end=end_date
)

st.write(ticker_data)
