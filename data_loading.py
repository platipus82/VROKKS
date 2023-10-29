import pandas as pd

def give_stock_data(stock, start_year=2015):
    # Define the file path for stock data
    stock_file = 'Data/Archive/Stocks/' + stock + '.us.txt'

    # Load the data into a pandas DataFrame
    stock_data = pd.read_csv(stock_file)

    # Convert the 'Date' column to a datetime object
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # Filter data after the specified start year
    stock_data = stock_data[stock_data['Date'].dt.year >= start_year]

    # Calculate daily percentage change in Close price
    stock_data['Daily_Return'] = stock_data['Close'].pct_change() * 100

    # Create a new feature: interaction between volume and price change
    stock_data['Volume_Price_Interact'] = stock_data['Volume'] * stock_data['Daily_Return']

    # Discard the first row (index 0) to remove data with NaN values
    stock_data = stock_data.iloc[1:]

    return stock_data



def give_event_data(stock_data, event_threshold=-1):
    # Calculate daily percentage change in Close price
    stock_data['Daily_Return'] = stock_data['Close'].pct_change() * 100

    # Set threshold values for events
    threshold = event_threshold

    # Create 'event' for a dip larger than argument threshold
    stock_data['event'] = stock_data['Daily_Return'] <= threshold

    # Display the modified DataFrame
    stock_data.head()

    return stock_data