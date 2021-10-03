# Nerlove OLS
Multivariate OLS linear regression on electric supply data.
Based on an exercise in Econometrics by Fumio Hayashi.
Data souce: http://fhayashi.fc2web.com/datasets.htm

### data_creator.py
Creates data for multiple linear regression from the 'nerlove.xls' dataset.

### ols_model.py
Performs multiple linear regression with OLS on the data imported from 'data_creator.py'.
OLS is performed with matrix algebra functions of numpy.

### main.py
Executes the OLS model from 'ols_model.py'.

### plotting.py
Does scatterplots of the explained variable (total costs) wrt. the explaining variables.
Run separetely from other scripts. Saves the plots to 'figures' folder.
