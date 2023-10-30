import matplotlib.pyplot as plt
from matplotlib.lines import Line2D  # Import Line2D
from matplotlib.dates import DateFormatter


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


def plot_stock_price_with_events(stock_data, stock_name="aapl", y_pred=None):
    plt.figure(figsize=(10, 6))

    # Create a boolean mask for events
    event_mask = stock_data['event']

    # Plot the Close prices in blue
    plt.plot(stock_data['Date'], stock_data['Close'], color='blue', label='Close Price')

    # Highlight actual events by coloring them in red
    plt.plot(stock_data['Date'][event_mask], stock_data['Close'][event_mask], color='red', marker='o', linestyle='', label='Event')

    if y_pred is not None:
        # Plot predicted values in green
        plt.plot(stock_data['Date'], stock_data['Close'] * y_pred, color='green', marker='^', linestyle='', label='Predicted')

    plt.title(f'Stock {stock_name}: Close Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Add a legend to distinguish between Close Price, Events, and Predictions
    plt.legend()

    plt.show()


def plot_stock_price_with_events_and_risk(stock_data, stock_name="aapl", y_pred=None):
    risk = tell_modelled_risk() 
    risk_text = "Predicted risk for anticipated event is " + str(risk)

    # Create a figure with two subplots: one for the main plot and one for text/legend
    fig, ax1 = plt.subplots(2, 1, gridspec_kw={'height_ratios': [4, 1]}, figsize=(10, 6))

    # Create a boolean mask for events
    event_mask = stock_data['event']

    # Plot the Close prices in blue
    ax1[0].plot(stock_data['Date'], stock_data['Close'], color='blue', label='Close Price')

    # Show events with dashed vertical lines and solid circles at y=0
    for date, is_event, close_price in zip(stock_data['Date'], event_mask, stock_data['Close']):
        if is_event:
            ax1[0].plot([date, date], [0, close_price], color='red', linestyle='--', linewidth=1, alpha=0.3)  # Dashed red line at event date with adjusted thickness and transparency
            ax1[0].plot(date, 0, 'ro', markersize=8)  # Solid red circle at y=0 at event date

    if y_pred is not None:
        # Plot predicted values in green with empty symbols and red borders
        ax1[0].plot(stock_data['Date'], [0] * len(stock_data['Date']), color='red', marker='o', linestyle='', label='Predicted', markersize=8, markeredgecolor='red', markerfacecolor='none')

    ax1[0].set_title('Stock ' + stock_name + ': Close Prices Over Time')
    ax1[0].set_ylabel('Close Price')

    # Set x-axis tick labels in the bottom panel to display only the year
    date_format = DateFormatter("%Y-%m-%d")
    ax1[0].xaxis.set_major_formatter(date_format)
    #plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    # Rotate x-axis labels for better readability
    ax1[0].tick_params(axis='x', rotation=45)
    
    # Add x-axis label
    ax1[0].set_xlabel('Date')

    # Create a separate panel for the legend and text
    ax2 = plt.subplot(212)

    # Hide axes
    ax2.axis('off')

    # Add the legend to the separate panel
    close_price_legend = Line2D([0], [0], color='blue', linestyle='-', label='Close Price')
    event_legend = Line2D([0], [0], color='red', linestyle='--', linewidth=1, alpha=0.3, label='Event')
    predicted_legend = Line2D([0], [0], color='red', marker='o', linestyle='', label='Predicted', markersize=8, markeredgecolor='red', markerfacecolor='none')
    predicted_correctly_legend = Line2D([0], [0], color='red', marker='o', linestyle='', label='Predicted correctly', markersize=8, markeredgecolor='red', markerfacecolor='red')

    ax2.legend(handles=[close_price_legend, event_legend, predicted_legend, predicted_correctly_legend], loc='upper left')

    # Add the risk_text to the right side of the legend
    legend = ax2.get_legend()
    legend.set_bbox_to_anchor((0.79, 0.74))

    ax2.text(0, 0, risk_text, fontsize=12, color='black')

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
