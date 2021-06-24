import pandas as pd
import numpy as np 

#file upload 
Data_file = 'AcinetobacterNIH.tsv'
Acine_data= pd.read_csv(Data_file, sep='\t')

#local variables
count = 0
index = 0
array_cities = []
sampleHosts = []
Date = Acine_data.iloc[:,5]
location = Acine_data.iloc[:,6]
sample_hosts = Acine_data.iloc[:,1]

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
            
  
#print statements    
print("The dataset has data from: "+str(Date.min()) + " and until "+Date.max())
print("The dataset has data from "+ str(count)+" unique cities")
print("The dataset has "+ str(index)+" unique sample hosts ")    