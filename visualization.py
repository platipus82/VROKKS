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

def plot_stock_price_with_events(stock_data, stock_name="aapl"):
    # Plotting the Close prices over time
    plt.figure(figsize=(10, 6))

    # Create a boolean mask for events
    event_mask = stock_data['event']

    # Plot the Close prices in blue
    plt.plot(stock_data['Date'], stock_data['Close'], color='blue', label='Close Price')

    # Highlight events by coloring them in red
    plt.plot(stock_data['Date'][event_mask], stock_data['Close'][event_mask], color='red', marker='o', linestyle='', label='Event')

    plt.title('Stock ' + stock_name + ': Close Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Add a legend to distinguish between Close Price and Events
    plt.legend()

    plt.show()

def plot_stock_price_with_events_and_risk(stock_data, stock_name="aapl"):
    from matplotlib.lines import Line2D  # Import Line2D

    risk = tell_modelled_risk() 
    risk_text = "Predicted risk for anticipated event is " + str(risk)

    # Plotting the Close prices over time
    plt.figure(figsize=(10, 6))

    # Create a boolean mask for events
    event_mask = stock_data['event']

    # Plot the Close prices in blue
    plt.plot(stock_data['Date'], stock_data['Close'], color='blue', label='Close Price')

    # Show events with vertical red lines
    for date, is_event, close_price in zip(stock_data['Date'], event_mask, stock_data['Close']):
        if is_event:
            plt.plot([date, date], [0, close_price], color='red', linestyle='-', linewidth=1, alpha=0.5)  # Solid red line at event date with adjusted thickness and transparency

    plt.title('Stock ' + stock_name + ': Close Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Add the risk_text as an annotation to the plot
    plt.text(stock_data['Date'].iloc[0], stock_data['Close'].max() * 0.85, risk_text, fontsize=12, color='black')

    # Add a legend to distinguish between Close Price and Events
    close_price_legend = Line2D([0], [0], color='blue', linestyle='-', label='Close Price')
    event_legend = Line2D([0], [0], color='red', linestyle='-', linewidth=1, alpha=0.5, label='Event')
    plt.legend(handles=[close_price_legend, event_legend], loc='upper left')    # You can specify a different location for the legend

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
