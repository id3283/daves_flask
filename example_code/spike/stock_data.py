import yfinance as yf

# Define the ticker symbol and the desired time period
ticker = 'AAPL'
start_date = '2024-07-25'
end_date = '2024-07-28'

# Download hourly data
data = yf.download(ticker, start=start_date, end=end_date, interval='1h')

# Display the first few rows of the data
print(data.head())