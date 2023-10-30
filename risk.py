from data_loading import give_stock_data, give_event_data
from model_training import train_first_model
from visualization import plot_stock_price, plot_stock_price_with_events, calculate_event_frequency

def main():
    default = input("Run with default arguments? (y/n): ").lower()
    while default not in ['y', 'n']:
        default = input("Please enter 'y' or 'n': ").lower()

    if default == "y":
        stock_name = "aapl"
        event_t = -1
        n_splits = 20
        n_estimators = 150
    else:
        stock_name = input("Enter the stock ID (e.g., aapl): ").lower()
        event_t = -float(input("Enter the event threshold (e.g., 1 for 1% dip): "))
        n_splits = int(input("Enter the number of splits for time series cross-validation: "))
        n_estimators = int(input("Enter the number of estimators for the Random Forest model: "))

    # Load stock data based on user input
    train_data, test_data = give_stock_data(stock=stock_name)

    # Calculate event data based on a threshold
    train_data = give_event_data(train_data, event_threshold=event_t)
    test_data = give_event_data(test_data, event_threshold=event_t)

    # Calculate event frequency
    calculate_event_frequency(train_data, event_threshold=event_t)

    # Train model
    risk_model = train_first_model(train_data, n_splits=n_splits, n_estimators=n_estimators)

    # Make predictions
    print("---making predictions---")
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Volume_Price_Interact']
    new_data = test_data
    X_new = new_data[features]
    y_pred_new = risk_model.predict(X_new)

    # Plot events and predicted events
    plot_stock_price_with_events(test_data, stock_name=stock_name, y_pred=y_pred_new)

if __name__ == "__main__":
    main()

