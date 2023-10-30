# VROKKS
**General.** To run the VROKKS tool, please, run the main program from script risk.py   
**Data.** US historical stock prices with earnings data dataset from Kaggle.
**ML-models.** Random forest.

# Data
We used dataset readily available from Kaggle:
  - https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs/

...but we have considered several others readily available datasets
- https://www.kaggle.com/datasets/tsaustin/us-historical-stock-prices-with-earnings-data/discussion
- https://www.kaggle.com/datasets/paultimothymooney/stock-market-data 3.
- https://rapidapi.com/collection/finviz-api 

...and APIs:
xxx

This model does have some restrictions:
  - The output visualization of the model provides multiple incorrect predictions for stock price events.
    However it does predict all of the events that truly occurred correctly.
    
  - The events, so stock price drops, are only observed considering whether or not they cross the daily threshold of -1%, -10% or other value drop. 
    This means that the day before and after are not looked at. 
    So if for example during a multiple days span the stock price drops, but the daily threshold is not ever crossed, the model doesn't take it into account as a price drop / event.       
