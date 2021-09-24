#Background information and data retrieval
import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://MLResources.rennecastro.repl.co/2019_2015HappinessReport.csv")
df.head()