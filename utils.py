import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import Input
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.metrics import RootMeanSquaredError as rms
from tensorflow.keras.metrics import MeanAbsoluteError as mae
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np

def get_df(name):
    return pd.read_csv(name)

def minNormalize(d, minVal=None, maxVal=None):
    '''
    Normalizes data between 0 and 1 for ML algorithms
    
    d [np.array] : dataset to normalize
    minVal [np.Array] : Array with minimum values to normalize with
    maxVal [np.Array] : Array with max values to normalize with
    return : normalized dataset, minimum of dataset, maximum of dataset
    '''
    if type(minVal) is not np.ndarray:
        minVal = np.min(d)
        maxVal = np.max(d)
    return (d - minVal) / (maxVal - minVal), minVal, maxVal

def inverseMinNormalize(dNorm, minVal, maxVal):
    '''
    Denormalized ML outputs
    
    dNorm [np.array] : dataset to inverse normalize
    return : inversed normalize the data
    '''
    return dNorm * (maxVal - minVal) + minVal

# define a useful splitting function
def splitData(df, trainFrac=0.8, valFrac=0.10, testFrac=0.10, seed=None):
    '''
    Randomly splits a dataset into training, validation, and testing
    
    df [DataFrame]    : Pandas DataFrame of value for the ML model
    trainFrac [float] : fraction of data (between 0 and 1) to train model with
    valFrac [float]   : fraction of data (between 0 and 1) to validate model training with
    testFrac [float]  : fraction of data (between 0 and 1) to test the model with
    seed [int]        : random seed for reproducability, default is None
    
    returns           : Randomly split dataframe in order of training, validation, testing
    '''
    
    if trainFrac + valFrac + testFrac != 1:
        raise Exception('Your input fractions do not add up to 1!! Exiting...')
        return
    
    # randomly shuffle the dataframe
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    
    # split into three sets
    
    idx1 = int(trainFrac*len(df))
    idx2 = idx1 + int(valFrac*len(df))
    
    train = df.iloc[0:idx1]
    val = df.iloc[idx1:idx2]
    test = df.iloc[idx2:]
    
    return train, val, test

# define a function to build a model given some inputs
def buildModel(nLayers, activation='relu', loss='mse', optimizer='adam', metrics=[], nOutputs=1, nInputs=3, actLast='sigmoid'):
    '''
    Builds the Sequential model for ML
    Note: make this more complex with more options as needed
    
    nLayers [int] : number of dense layers
    activation [String] : activation function to use in each Dense layer
    loss [String] : loss function to use during compiling
    optimizer [String] : optimizer to use for training, default is adam
    metrics [List] : metrics to return from the model training
    nOutputs [int] : number of output values, used to set # of nodes in last layer
    actLast [String] : activation function to use in the last layer
    
    returns : a Keras Sequential Model object
    '''
    
    # initialize the model
    model = Sequential()

    nodes = 2**nLayers
    # start large than get smaller
    while nLayers > 0:
        if nLayers == 1:
            model.add(Dense(nOutputs, activation='sigmoid'))
        else:
            model.add(Dense(nodes, activation=activation))
        
        nodes = nodes/2
        nLayers -= 1
        
        
    # compile the model
    model.compile(loss=loss,
                 optimizer=optimizer,
                 metrics=metrics)
        
    return model