import pandas as pd

def give_stock_data(stock, start_year=2015):
    # Define the file path for stock data
    individual_stock_file = 'Data/Archive/Stocks/' + stock + '.us.txt'

    # Load the data into a pandas DataFrame
    individual_stock_data = pd.read_csv(individual_stock_file)

    # Convert the 'Date' column to a datetime object
    individual_stock_data['Date'] = pd.to_datetime(individual_stock_data['Date'])

    # Filter data after the specified start year
    individual_stock_data = individual_stock_data[individual_stock_data['Date'].dt.year >= start_year]

    return individual_stock_data

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