import numpy as np

def ols(X, y):
    """
    Calculates the OLS estimator of the given data. The calculations are
    done step by step.
    The OLS estimator 'b' is defined as:
    b = (X'X)^-1 * X'y
    """

    X_X = np.dot(X.T,X) # X'X
    X_X_inv = np.linalg.inv(X_X) # Inverse of X'X
    X_X_X = np.dot(X_X_inv, X.T) # Dot product of (X'X)^-1 and X'

    # Dot product of (X'X)^-1*X' & y, i.e., the OLS estimator
    b = np.dot(X_X_X, y)

    return b

def r_squared(X, y, b):
    """
    Calculates the coefficient of determination of the model.
    The coefficient of determination is defined as:
    1 - e'e/y'y
    """
    x_b = np.dot(X, b) # Xb
    e = y - x_b # Residual
    r_uc = 1 -  np.dot(e.T, e) / np.dot(y.T, y)

    return r_uc
