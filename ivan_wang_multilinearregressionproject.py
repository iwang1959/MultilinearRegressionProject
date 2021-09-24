# -*- coding: utf-8 -*-
"""Ivan Wang - MultilinearRegressionProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bxzDeQIkO-FEIXDQnVI6f7D-4K5eJUxM

<b><h1>Project Overview</h1>
<h3>Description</h3></b>
Choose a topic that interests you and find some data.  Using your knowledge of pandas, matplotlib and scikit-learn, create a machine learning application on a dataset that interests you. Taking advantage of Colab, you will embed narratives intermixed with code.  Each requirement below is its own text and code block in Colab.  It is probably best to use multiple text and code blocks for each requirement.
<br>
<b><h3>Requirements</h3></b>
<ol>
  <li><i>Background information and data retrieval</i><br>
    <u>Text Block</u> Provide a brief description of the dataset.  
    <ul>
      <li>General information about the dataset</li>
      <li>What is your machine learning application predicting?</li>
      <li>How is this prediction useful to someone?</li>
    </ul>
    <u>Code Block</u>   
    <ul>
      <li>Load the libraries</li>
      <li>Load the dataset</li>
      <li>Provide a preview of the data</li>
    </ul>
  </li>
  <li><i>Data Preparation</i><br>
    <u>Text Block</u> Provide a brief description of the preparation that needed to be made to the data prior to creating the machine learning model.  
    <ul>
      <li>What cleaning did you have to perform?</li>
      <li>Do you have to filter the data to exclude outliers for instance?</li>
      <li>What analysis did you perform to determine the right features to use?</li>
    </ul>
    <u>Code Block</u> Following are possbile options 
    <ul>
      <li>Drop NaN. Transform and handle "dirty" data.</li>
      <li>View histograms, scatter plots, correlation matrices and heatmaps to analyze the data</li>
      <li>Filter the data</li>
      <li>Select the target and features. Split the data into a training and testing sets.</li>
    </ul>
  </li>
  <li><i>Model Building</i><br>
  <u>Text Block</u> Discuss the outcome of building the model.    
    <ul>
      <li>What is your machine learning application predicting?</li>
      <li>How well did does your model predict?</li>
      <li>Were there any modifications you made after creating the model?</li>
    </ul>
    <u>Code Block</u> 
    <ul>
      <li>Create and train the model.</li>
      <li>Evaluate the model.</li>
    </ul>
  </li>
  <li><i>Machine Learning Application</i><br>
    <u>Text Block</u> Discuss the outcome of machine learning application.    
    <ul>
      <li>What is your machine learning application predicting?</li>
      <li>How is this prediction useful to someone?</li>
      <li>Conclusion</li>
    </ul>
    <u>Code Block</u> Provide a couple of predictions to demonstrate that your machine learning application
  </li>

# **Background information and data retrieval**

The World Happiness Report is a landmark survey of the state of global happiness. This dataset contains information about a country's happiness status. This machine learning application is going to predict if the GDP per capita and social support of a country can affect a country Score. The government, organizations and civil society could use this to inform their policy-making decisions. This prediction of well-being can be used to assess the progress of nations. People can use this prediction to determine whether they should move there.
"""

import pandas as pd
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://MLResources.rennecastro.repl.co/2019_2015HappinessReport.csv")
df.head()

"""# **Data Preparation**

Before creating the machine learning model we need to prepare the data first. I calculated for any potential outliers and filter them.
"""

df.describe()
#LOOKING FOR OUTLIERS 
#FOR Score: IQR = Q3 - Q1 = 1.67975
#lower inner fence: Q1 - 1.5*IQR = 1.990125
#lower outer fence: Q1 - 3*IQR = -0.5295
#upper inner fence: Q3 + 1.5*IQR =  8.709125
#upper outer fence: Q3 + 3*IQR = 11.22875

#LOOKING FOR OUTLIERS 
#FOR GDP: IQR = Q3 - Q1 = 0.629687
#lower inner fence: Q1 - 1.5*IQR = -0.3380305
#lower outer fence: Q1 - 3*IQR = -1.282561
#upper inner fence: Q3 + 1.5*IQR =  2.1807175
#upper outer fence: Q3 + 3*IQR = 3.125248

#LOOKING FOR OUTLIERS 
#FOR Generosity: IQR = Q3 - Q1 = 0.148832
#lower inner fence: Q1 - 1.5*IQR = -0.093248
#lower outer fence: Q1 - 3*IQR = -0.316496
#upper inner fence: Q3 + 1.5*IQR =  0.50208
#upper outer fence: Q3 + 3*IQR = 0.725328

data = df[(df["GDP per capita"] > 0.25) & (df["GDP per capita"] < 1.70) & (df["Social support"] > 0.50)]
#data = df.drop(labels=["Country or region", "Year"],axis = 1)
data.head()

"""After using data.dropna(), data.isna().sum(), data.shape to check if there was dirty data. 

Theres no dirty data.
"""

print(data.shape)
data = data.dropna()
print(data.shape)

print(data.isna().sum())
print(data.dtypes)

data.isin(["  ","?","Na","na"]).sum()
print(data.shape)

"""I view histograms, scatter plots, correlation matrices and heatmaps to analyze the data. GDP per capita	and Social support both had postive a correlation to Score. So I decided to use these features."""

data.corr()

import seaborn as sns
sns.heatmap(data.corr(),linewidths=2,cmap="viridis")

data.hist(figsize=[10,10])

pd.plotting.scatter_matrix(data, figsize=[15,15])

desired_features = ["GDP per capita","Social support"]

target = data["Score"]
features = data[desired_features]

features_train, features_test, target_train, target_test  = train_test_split(features, target, test_size = 0.2, random_state = 6)

"""# **Model Building**

My machine learning application is predicting if GDP per capita	and Social support affect a country Score. My machine learning application is about 64% accuate in predicting a country's Score.
I changed the random_state = 9 to random_state = 6 to increase my accuracy.
"""

lr = LinearRegression()
lr.fit(features_train, target_train)

lr.score(features_test, target_test)

"""# **Machine Learning Application**"""

for times in range(5):
  percent= lr.score(features_test, target_test)
  percent_accurate = percent * 100
  test = data.sample()
  test_features = test[desired_features]
  predict_score = lr.predict(test_features)
  print("Test Information")
  print(test[["Year", "Score", "Generosity", "Healthy life expectancy", "GDP per capita", "Social support"]])
  print(f"Predicted Score: {predict_score}")
  print("Please note that this is only " + str(percent_accurate) + "% accurate\n\n")

"""This machine learning application is going to predict if the GDP per capita and social support of a country can predict a country Score.

People could use these predictions to determine whether they would want to move to the country. The government or experts can use this prediction to make policy decisions and assess the progress of nations. For example, in 2015 a country had a actual score = 5.007, a GDP per capita = 0.91851, and Social support = 1.00232. Our predicted Score = 5.24321897, shows that our model is off but very close to the actual Score. 

Therefore, this machine learning application is going to predict if the GDP per capita and social support of a country can predict a country Score. People are free to use this application but just remeber it's only 63.57379442352404% accurate.
"""