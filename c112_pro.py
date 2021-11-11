# -*- coding: utf-8 -*-
"""c112.pro

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bs1l67LguQIyNk8f7KarLjGWKUlQU3yR
"""

from google.colab import files
data_to_load=files.upload()

import pandas as pd
import plotly.express as px
import statistics
import csv
import random
import numpy as np


df=pd.read_csv(r"savings_data.csv")

fig=px.scatter(df,y="quant_saved",color="female")
fig.show()

quant_saved=df["quant_saved"]


mean=statistics.mean(quant_saved)
median=statistics.median(quant_saved)
mode=statistics.mode(quant_saved)
sd=statistics.stdev(quant_saved)

print("mean of all quant_saved:",mean)
print("median of all quant_saved:",median)
print("mode of all quant_saved:",mode)

print("\n")

sampling_1=[]
for i in range(0,100):
  randomIndex=random.randint(0,len(quant_saved)-1)
  dataValue=quant_saved[randomIndex]
  sampling_1.append(dataValue)

sampling_2=[]
for i in range(0,100):
  randomIndex=random.randint(0,len(quant_saved)-1)
  dataValue=quant_saved[randomIndex]
  sampling_2.append(dataValue)

sampling1Mean=statistics.mean(sampling_1)
sampling2Mean=statistics.mean(sampling_2)
sampling1SD=statistics.stdev(sampling_1)
sampling2SD=statistics.stdev(sampling_2)

print("mean of sampling 1:",sampling1Mean)
print("mean of sampling 2:",sampling2Mean)
print("mean of population:",mean)

print("\n")

print("SD of sampling 1:",sampling1SD)
print("SD of sampling 2:",sampling2SD)
print("SD of population:",sd)

wealthy=df["wealthy"]

correlation=np.corrcoef(wealthy,quant_saved)

print("correlation of welthy and savings:",correlation[0,1])