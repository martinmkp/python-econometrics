import numpy as np
import pandas as pd

def create_data(path: str):
    """
    Reads the data into a pandas dataframe. The, each variable
    is saved to numpy arrays, and transformed to log-form.
    Finally, the explanatory variables are stacked to a single matrix.
    """

    df = pd.read_excel(path) # Reads the dataset

    tc = df.iloc[:,0].values # Total costs in million $
    tc_log = np.log(tc)

    q = df.iloc[:,1].values # Output in billions of kWh
    q_log = np.log(q)

    pl = df.iloc[:,2].values # Price of labor
    pl_log = np.log(pl)

    pf = df.iloc[:,3].values # Price of fuels
    pf_log = np.log(pf)

    pk = df.iloc[:,4].values # Price of capital
    pk_log = np.log(pk)

    # In addition, we need a vector of 1s to reprecent intercept
    inter = np.ones(len(tc))

    # Stacks the 5 vectors of explanatory variables to a nx5 matrix X
    X = np.stack((inter, q_log, pl_log, pf_log, pk_log), axis=-1)

    # Save the explained variable tc_log to a column vector y
    y = tc_log.T

    return X, y
