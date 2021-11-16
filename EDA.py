#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os                    #importing os
import pandas as pd          #importing pandas
import numpy as np           #importing numpy


# **The below EDA Function will return Statistics about the given Data based on the inputs Given.**
# 
# **Manadatory Parameters -**
# 
# *1 .File - Dataset on which EDA to be performed.*
# 
# **Optional Parameters -**
# 
# *2 .Correlation_check - would return a correlation matrix for all numeric columns in the data set.*
# 
# *3 .null_values - would check and return the sum of null values present for all the variables in the Dataset.*
# 
# *4 .columns_with_correlation - this parameter will return a correlation matrix only for those variables which have +ve or -ve 
# correlation user can specify the threshold for correlation coeffecient.*
# 
# *5 .correlation_threshold - using this user can alter the threshold for correlation ie. applicable for parameter "4" - 
#     Default threshold = 0.5*
#     
# **If no optional parameters are given by default it would return the descreptive statistics of all numeric columns in the Dataset.**

# In[18]:


def EDA(file,                                       #file for which EDA needs to be Done
        Descreptive_statistics_columns = None,      # if user wants EDA to be done only for specific columns in the Data set
        Correlation_check = None,                   # if user wants to check for correlation among all the numeric columns in Dataset 
        null_values = None,                         # if user wants to check for null values for all the columns 
        columns_with_correlation = None             # if user wants to check correlation only for variables which showed correlation
        ,correlation_threshold = 0.5):              # if user wants to modify the threshold for correlation coffecient for 
                                                    # the optional parameter columns_with_correlation
    
    

    
    if Descreptive_statistics_columns == None:             #if column names given
        
        file = file[file.columns]
        
        numeric = file.select_dtypes(include = np.number)      #seperating numeric columns
        
        Descreptive_statistics = numeric.describe()        #get descreptive statistics
        
    else:
        file = file[Descreptive_statistics_columns]       #if columns specified
        
        numeric = file.select_dtypes(include = np.number) #seperating numeric columns
        
        Descreptive_statistics = numeric.describe()   #get descreptive statistics for all columns
        
        
    if Correlation_check == 1:                #if correlation check is given 1
        
        correlation = numeric.corr()          #getting correlation matrix for all the numeric columns
        
    else:
        
        correlation = None                   #else setting it as none
        
    if null_values == 1:                     #if null value check is given
        
        null = np.sum(file.isnull())         #getting null values in the dataset
    else: 
        
        null = None                          #else setting it as none
        
    if columns_with_correlation != None:  #if check_for_correlated_columns_given value check is given
        list = []                         #appending the co-rrelated columns into the list
        k = 0                             #setting counter for k as zero
        while k < (numeric.shape[1] - 1): #running a while loop     
                for i in range(numeric.shape[1]):     #running a for loop
                        if i != k:                    #setting up a check so, that same columns are not selected
                            corr = numeric[[numeric.columns[k],numeric.columns[i]]].corr()  #checking correlation for individual columns
                            if (corr.loc[numeric.columns[k]][1] > correlation_threshold):   #seperating columns with co-rrelation above threshold
                                list.append(numeric.columns[i])                             #appending the columns that have higher threshold
                            if (corr.loc[numeric.columns[k]][1] < -(correlation_threshold)):#seperating columns with co-rrelation above threshold
                                list.append(numeric.columns[i])                             #appending the columns that have higher threshold
                k += 1                                                                      #setting counter for k
                df = pd.DataFrame({"list":list})                                            #creating a dataframe of column names
                
        Correlation_columns1 = numeric[df.list.unique()].corr()                             #seperating unique column names
    else:
        Correlation_columns1 =  None    #else setting it as none 
        
    #below created out put for all possible combinations of parameteres function will return output based on the given parameteres     
     
    # if all of the optional parameteres are true 
    
    if (Correlation_check != None) & (null_values != None) & (columns_with_correlation != None):
        
        return(Descreptive_statistics,correlation,null,Correlation_columns1)
    
    # if Correlation_check is true
    
    if (Correlation_check != None) & (null_values == None) & (columns_with_correlation == None):
        
        return(Descreptive_statistics,correlation)
    
    # if null_values is true
    
    if (Correlation_check == None) & (null_values != None) & (columns_with_correlation == None):
        
        return(Descreptive_statistics,null)
    
    # if columns_with_correlation is true
    
    if (Correlation_check == None) & (null_values == None) & (columns_with_correlation != None):
        
        return(Descreptive_statistics,Correlation_columns1)
    
    # if columns_with_correlation is true
    
    if (Correlation_check != None) & (null_values != None) & (columns_with_correlation == None):
        
        return(Descreptive_statistics,correlation,null)
    
    # if Correlation_check and columns_with_correlation is true
    
    if (Correlation_check != None) & (null_values == None) & (columns_with_correlation != None):
        
        return(Descreptive_statistics,correlation,Correlation_columns1)
    
    # if null_values and columns_with_correlation is true
    
    if (Correlation_check == None) & (null_values != None) & (columns_with_correlation != None):

        return(Descreptive_statistics,null,Correlation_columns1)  
    
    else:
        
        return(Descreptive_statistics)      #if no arguments given will return default descreptive statistics for the dataset      

