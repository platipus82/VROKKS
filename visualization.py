import matplotlib.pyplot as plt

def plot_stock_price(stock_data, stock_name="aapl"):
    # Plotting the Close prices over time
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Date'], stock_data['Close'], color='blue')
    plt.title('Stock ' + stock_name + ': Close Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()

def calculate_event_frequency(stock_data, event_threshold):
    # Calculate frequency of event1 (1% dip) and event2 (10% dip)
    event_count = stock_data['event'].sum()
    #event2_count = apple_stock_data['event2'].sum()

    # Total number of data points
    total_data_points = len(stock_data)

    # Calculate frequencies
    event_frequency = event_count / total_data_points
    #event2_frequency = event2_count / total_data_points
    dip_size = str(-event_threshold)
    #print(f"Frequency of " + dip_size + "% dip (event1): {event1_frequency * 100:.2f}%")
    print(f"Frequency of {dip_size}% dip (event): {event_frequency * 100:.2f}%")
