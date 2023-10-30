import warnings
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.dummy import DummyClassifier

# Suppress warnings
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

def train_first_model(stock_data, n_splits=15, n_estimators=100):
    print("-----training the model-----")
    metrics = {
        'accuracy': [],
        'f1_score': [],
        'precision': [],
        'recall': [],
        'accuracy_dummy': [],
        'f1_score_dummy': [],
        'precision_dummy': [],
        'recall_dummy': []
    }

    # Features (X) and Target variable (y)
    # Considering 'Open', 'High', 'Low', 'Close', 'Volume' as features for simplicity
    features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Volume_Price_Interact']
    X = stock_data[features]
    y = stock_data['event']

    # Initialize TimeSeriesSplit
    tscv = TimeSeriesSplit(n_splits=n_splits)

    # Initialize Random Forest model
    forest_model = RandomForestClassifier(n_estimators=n_estimators)  # You can adjust parameters

    # Initialize DummyClassifier for comparison
    dummy_model = DummyClassifier(strategy="most_frequent")

    # Perform time series cross-validation
    for train_index, test_index in tscv.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        forest_model.fit(X_train, y_train)
        y_pred = forest_model.predict(X_test)
        print("...", end=" ")

        # Train and evaluate the DummyClassifier
        dummy_model.fit(X_train, y_train)
        y_pred_dummy = dummy_model.predict(X_test)

        # Calculate metrics for each split
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)

        # Calculate dummy classifier metrics
        accuracy_dummy = accuracy_score(y_test, y_pred_dummy)
        f1_dummy = f1_score(y_test, y_pred_dummy)
        precision_dummy = precision_score(y_test, y_pred_dummy)
        recall_dummy = recall_score(y_test, y_pred_dummy)

        # Append the metrics to the list
        metrics['accuracy'].append(accuracy)
        metrics['f1_score'].append(f1)
        metrics['precision'].append(precision)
        metrics['recall'].append(recall)

        metrics['accuracy_dummy'].append(accuracy_dummy)
        metrics['f1_score_dummy'].append(f1_dummy)
        metrics['precision_dummy'].append(precision_dummy)
        metrics['recall_dummy'].append(recall_dummy)

        # Calculate average metrics
    avg_metrics = {metric: sum(values) / len(values) for metric, values in metrics.items()}
    print("\nAverage Metrics:")
    for metric, value in avg_metrics.items():
        print(f"{metric.capitalize()}: {value:.4f}")
    return forest_model

def tell_modelled_risk():
    ''' Risk in range 0...100, 0 representing 0 risk, and 100 representing 100% certainty '''
    return 42
