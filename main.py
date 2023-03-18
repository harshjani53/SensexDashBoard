import streamlit as stL
import yfinance as yahooFin
import pandas as pan
stL.title("Stocks Returns Dashboard(Top Sensex Stocks)")

stocks = ("^BSESN","ASIANPAINT.BO","AXISBANK.BO","BAJAJ-AUTO.BO","BAJAJ FINSERV","BHARTI AIRTEL",
           "BHARTIARTL.BO","DRREDDY.BO","HCLTECH.BO","	HDFC.BO","HDFCBANK.BO",
           "HINDUNILVR.BO","ICICIBANK.BO","INDUSINDBK.BO","	INFY.BO","ITC.BO","KOTAKBANK.BO",
           "LT.BO","M&M.BO","MARUTI.BO","NESTLEIND.BO","NTPC.BO","ONGC.BO",
           "POWERGRID.BO","RELIANCE.BO","SBIN.BO","SUNPHARMA.BO","TCS.BO","TECHM.BO",
           "TITAN.BO","ULTRACEMCO.BO")

dropdownMenu = stL.multiselect("Pick your stock ", stocks)

startDate = stL.date_input("Start Date", value = pan.to_datetime('2022-01-01'))
endDate = stL.date_input("End Date", value = pan.to_datetime('today'))

if(startDate > endDate):
    e = RuntimeError('''End Date must be after Start Date. 
                     Pick Change Start-Date or End-Date''')
    stL.exception(e)
def returns(df):
    relative = df.pct_change()
    cumulativeReturns = (1+relative).cumprod()-1
    cumulativeReturns = cumulativeReturns.fillna(0)
    return cumulativeReturns

if len(dropdownMenu) > 0:
   df = returns(yahooFin.download(dropdownMenu,startDate,endDate)['Adj Close'])
   stL.header(f'Returns of {dropdownMenu}\n from {startDate} to {endDate}' )
   stL.line_chart(df)
