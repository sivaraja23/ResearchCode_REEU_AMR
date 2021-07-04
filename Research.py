import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import random 
import seaborn as sns
import string 
#file upload 
Data_file = 'AcinetobacterNIH.tsv'
Acine_data= pd.read_csv(Data_file, sep='\t')

#local variables
count = 0
index = 0
a = 0
array_cities = []
sampleHosts = []
Date = Acine_data.iloc[:,5]
date_time_dataset = pd.to_datetime(Date)
location = Acine_data.iloc[:,6]
acro_location = []
sample_hosts = Acine_data.iloc[:,1]
acro_hosts = []
year = date_time_dataset.dt.year
translation_table = str.maketrans('', '', string.digits)
#Analysis
for val in location:
    if val != "USA":
        if val not in array_cities:
            count+=1
            array_cities.append(val)
  
for val in sample_hosts:
    if val not in sampleHosts:
        index+=1
        sampleHosts.append(val)
for index,value in location.items():
         value = "".join(e[0].upper() for e in value.split())
         if value == 'U':
             value = 'USA'
         acro_location.append(value)

#graphing 
#plots the frequency of location 
colour = ['yellowgreen','red','gold','lightskyblue','white','lightcoral','blue','pink', 'darkgreen','yellow','grey','violet','magenta','cyan','tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan','wheat','oldlace','floralwhite','darkgoldenrod','lightcyan','darkturquoise','indigo','darkviolet','purple','lightcoral','fuchsia','cyan','darkcyan','cadetblue','teal','turquoise','aquamarine','slategray','royalblue','ghostwhite','cornsilk','hotpink','tomato','mistyrose','darksalmon','orangered','aliceblue','palegreen','honeydew','greenyellow','darkolivegreen','bisque','burlywood','tan','papayawhip','beige','ivory','khaki','darkkhaki','peru','sandybrown','saddlebrown']
rand_colours = [random.choice(colour) for i in range(50)]
fig, ax = plt.subplots()
df = pd.Series( (v for v in acro_location) )
df.value_counts().plot(ax=ax, kind='bar', xlabel='location', ylabel='frequency', color = rand_colours)
plt.show()
#plots the frequency of sample hosts 
sample_hosts.value_counts().plot(ax=ax, kind='line', xlabel='sample hosts', ylabel='frequency', color = rand_colours)
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.show()
#plots the frequency of the years
year.value_counts().plot(ax=ax, kind='bar', xlabel='year', ylabel='frequency')
plt.show()

  
#print statements    
print("The dataset has data from: "+str(Date.min()) + " and until "+Date.max())
print("The dataset has data from "+ str(count)+" unique cities")
print("The dataset has "+ str(index)+" unique sample hosts ")    