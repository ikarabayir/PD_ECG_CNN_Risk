#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os
import sys
import joblib
import glob
import numpy as np
from scipy import signal
import pandas as pd 
import keras

thr = 0.139
print ('Models are loading..!')
#models = glob.glob('Model_CNN\*.h5') #CNN models
model = 'Model_CNN/Settled_3_yearX_pd_visit_count2_v499_10_5_12.h5'

print ('Datasets are loading..!')
ECG_file = np.load(sys.argv[1], allow_pickle = True)
ECG_file=ECG_file[::,250:,] # Cut first second



print ('ECG resampling done!')

print ('Getting CNN predictions ...')

model = keras.models.load_model(model)
CNN_predictions = model.predict(ECG_file)
       

     
binary_pred = np.array([1 if i > thr else 0 for i in CNN_predictions[:,1]])

print ('Saving predictions...')
       
with open("risk_predictions.csv", "w") as file:
    file.write(str(CNN_predictions[:,1]))


with open("binary_predictions.csv", "w") as file:
    file.write(str(binary_pred))


# In[ ]:





# In[ ]:




