import numpy as np
import pandas as pd

from data_creator import create_data
from ols_model import ols



def main():
    path = "nerlove.xls" # Path for the dataset
    X, y = create_data(path)
    b = ols(X, y)

    return f"The OLS estimator is: b = {b}"


if __name__ ==  '__main__':
    print(main())
