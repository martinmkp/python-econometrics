import numpy as np
import pandas as pd

from data_creator import create_data
from ols_model import ols
from ols_model import r_squared



def main():
    path = "nerlove.xls" # Path for the dataset
    X, y = create_data(path)
    b = ols(X, y) # Ols estimator
    r_uc = r_squared(X, y, b) # Uncentered r-r_squared

    # Round down to 2 decimals
    b_rounded = [round(i, 2) for i in b]
    r_uc_rounded = round(r_uc, 2)
    return f"The OLS estimator is: b = {b_rounded}", f"The R-squared is: {r_uc_rounded}"


if __name__ ==  '__main__':
    print(main())
