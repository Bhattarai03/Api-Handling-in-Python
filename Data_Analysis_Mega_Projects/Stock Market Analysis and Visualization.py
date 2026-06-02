# Stock Market Analysis and Visualization
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import textwrap

dataframe=pd.read_csv("Stock Market Datasets.csv")
print(dataframe)

# For getting information of datasets
print(dataframe.shape)
print(dataframe.info())
print(dataframe.columns)
print(dataframe.describe())

# For checking missing value
print(dataframe.isnull().sum())

# For knowing datatype
print(dataframe.dtypes)


# For Calcuating 
'Moving Average of past  30 days'
dataframe["MA_30"]=dataframe["Close"].rolling(window=30).mean()
print("Moving Average")
print(dataframe["MA_30"])

'Daily Returns'
dataframe["Daily Return"]=dataframe["Close"].pct_change()
print("Daily Returns")
print(f"{dataframe["Daily Return"]}")

'Cumulative Return'
dataframe['Cumulative Return']=(1 + dataframe["Daily Return"]).cumprod()
print(dataframe["Cumulative Return"])

# Buy when signal ==1
dataframe['Signal'] = 0
dataframe.loc[dataframe['Close'] > dataframe['MA_30'], 'Signal'] = 1
print(dataframe["Signal"])


# Calculating Standard Deviation
dataframe["STD"] =dataframe["Daily Return"].std()
print(dataframe["STD"])

# Calculating Correlation
pivot_df=dataframe.pivot(index='Date',columns="Ticker",values="Close")
returns=pivot_df.pct_change().dropna()
corr_df=returns.corr()
print(corr_df)

# Annualized Volatility
daily_volatility=dataframe["Daily Return"].std()
annual_volatility=daily_volatility*np.sqrt(252)
print("Annual Volatility:",annual_volatility)

# Rolling Volatility
rollingvolatality=dataframe["Daily Return"].rolling(window=30).std()*np.sqrt(252)
print("Rolling Volatility of last 30 days")
print(f"{rollingvolatality}")



# Data Visualization
'Stock Price over time'
plt.figure(figsize=(10,9))
lineplot = dataframe[["Date", "Close"]].head(40)
lineplot['Date'] = pd.to_datetime(lineplot['Date'])
sns.lineplot(data=lineplot,x='Date',y='Close',color='blue')

plt.title("Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.grid(True)
plt.show()

'Daily Return Over Time'
plt.figure(figsize=(10,9))
lineplot2=dataframe[dataframe["Ticker"]=='AAPL'][["Daily Return","Date"]].head(40)
lineplot2["Date"]=pd.to_datetime(dataframe["Date"])
sns.lineplot(x='Date',y="Daily Return",data=lineplot2,color='blue')

plt.title("Daily Return Over Time of AAPL")
plt.xlabel("Date")
plt.ylabel("Daily Return")
plt.grid(True)
plt.show()


'Cumulative Return Over Time'
plt.figure(figsize=(10,8))
lineplot3=dataframe[dataframe["Ticker"]=="AAPL"][['Cumulative Return','Date']]
lineplot3["Date"]=pd.to_datetime(lineplot3["Date"])
sns.lineplot(x='Date',y="Cumulative Return",data=lineplot3,color='blue')
plt.title("Cumulative Return Over Time Of AAPL")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.grid(True)
plt.show()

'Rolling Stock Price Average'
Rollavg=dataframe[dataframe["Ticker"]=="AAPL"][["MA_30","Date"]]
print(Rollavg)
Rollavg["Date"]=pd.to_datetime(Rollavg["Date"])
plt.figure(figsize=(8,8))
sns.lineplot(data=Rollavg,x="Date",y="MA_30",color="yellow")
plt.title("Moving Average Stock Price of past 30 days of AAPL")
plt.xlabel("Date")
plt.ylabel("Moving Average")
plt.grid(True)
plt.show()

'Rolling Daily Return of past 30 days of AAPL'
dataframe["Rolling Daily Return"]=dataframe["Daily Return"].rolling(window=30).mean()

roll_daily_return=dataframe[dataframe["Ticker"]=="AAPL"][["Rolling Daily Return","Date"]]
roll_daily_return["Date"]=pd.to_datetime(roll_daily_return["Date"])
print(roll_daily_return)
plt.figure(figsize=(8,8))
sns.lineplot(data=roll_daily_return,x="Date",y="Rolling Daily Return",color="yellow")
plt.title("Moving Average Daily Return  of past 30 days of AAPL")
plt.xlabel("Date")
plt.ylabel("Moving Average Daily Return ")
plt.grid(True)
plt.show()

'Rolling Cumulative Return of past 30 days of AAPL'
dataframe["Rolling Cumulative Return"]=dataframe["Cumulative Return"].rolling(window=30).mean()

roll_cumu_return=dataframe[dataframe["Ticker"]=="AAPL"][["Rolling Cumulative Return","Date"]]
roll_cumu_return["Date"]=pd.to_datetime(roll_cumu_return["Date"])
print(roll_cumu_return)
plt.figure(figsize=(8,8))
sns.lineplot(data=roll_cumu_return,x="Date",y="Rolling Cumulative Return",color="yellow")
plt.title("Moving Average Cumulative Return  of past 30 days of AAPL")
plt.xlabel("Date")
plt.ylabel("Moving  Cumulative Return ")
plt.grid(True)
plt.show()

'Corelation Among Stocks'
plt.figure(figsize=(6,5))
sns.heatmap(corr_df,annot=True,cmap="coolwarm",fmt=".2f",)
plt.title("Correlation Between AAPL,MSFT, and TSLA")
plt.show()

'Line graph among stocks'
plt.figure(figsize=(8,13))
sns.lineplot(data=pivot_df, x='Date', y='AAPL', label='AAPL', marker='o')
sns.lineplot(data=pivot_df, x='Date', y='MSFT', label='MSFT', marker='s')
sns.lineplot(data=pivot_df, x='Date', y='NFLX', label='NFLX', marker='^')
sns.lineplot(data=pivot_df, x='Date', y='GOOG', label='GOOG', marker='d')

plt.title("Stock Prices Over Time")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

