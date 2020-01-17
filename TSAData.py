# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import statsmodels as sm
import tensorflow as tf
import quandl
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import logging

log_file_url= os.path.curdir + "/logs/debug.log"
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler(log_file_url, mode='w' )
f_handler.setLevel(logging.DEBUG)

logger.addHandler(f_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Open Logging")
#logging.basicConfig(filename='./logs/debug.log', filemode='w', level=logging.DEBUG
#                    ,format='%(name)s - %(levelname)s - %(message)s')

def main(ticker="TSLA"):
    quandl.ApiConfig.api_key = "tKJQ-CPXwKLLEzZBsv8o"
    data = None
    file_name = os.path.curdir +  "/datasets/fin/" +  "prices_" + ticker + ".csv"
    print ("File Name" + file_name)
    logger.debug("File path:" + file_name)
    if os.path.exists(file_name):
        logger.debug("File path exists, loading data from file")
        data = pd.read_csv(file_name)
        if data is None:
            logger.debug("Data is not loaded")
        else: 
            logger.debug("File loaded" )
    else:
        logger.debug("File not found. Loading data from service")
        data = load_data('AAPL')
        #Cols: Open, High. Low, lose, Volume, Ex-Divi, Adj. (Open, High, Low, Close, Volume)
        logger.debug ("Data loaded from service. " )
        print(data.head())
        data.to_csv(file_name, header=True, mode='w')   
        logger.debug("Saved data to file")

    if data is None:
        logger.debug ("No data found. Exiting")
        exit()
        
        
def load_data(tickr = 'TSLA', rows = 250):
    return quandl.get("WIKI/"+tickr, rows=rows)
    #data = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
    
'''
Recurrent neural network
A Recurrent Neural Network (RNN) is a type of neural network well-suited to time series data.
 RNNs process a time series step-by-step, maintaining an internal state summarizing 
 the information they've seen so far. For more details, read the RNN tutorial. 
 In this tutorial, you will use a specialized RNN layer called 
 Long Short Term Memory (LSTM)
'''
def model_train():
    None
    
logger.debug(__name__)
if __name__ == "__main__":
    logger.debug("Calling main")
    main("AAPL")