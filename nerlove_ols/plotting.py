import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from data_creator import create_data

def scatterplots():
    """
    Plots scatterplots with Pearson correlation
    coefficients from the given data.
    """
    path = "nerlove.xls"
    X, y = create_data(path) # Data
    corr = 0.0 # Variable for correlation

    title = ["Output","Wage rate","Fuel price","Price of capital"]
    for i in range(len(title)):
        corr = np.corrcoef(X[:,i+1] ,y)[0, 1]
        plt.figure()
        plt.scatter(X[:,i+1] ,y)
        plt.title("Scatterplot of log variables, Pearson corr: " + str(round(corr, 2)), fontsize = 18)
        plt.xlabel(title[i], fontsize = 15)
        plt.ylabel("Total costs", fontsize = 15)
        plt.savefig("../nerlove_ols/figures/scatter_TC_" + title[i] +".png")


if __name__ ==  '__main__':
    scatterplots()
