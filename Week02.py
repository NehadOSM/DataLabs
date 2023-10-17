# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:00:13 2023

@author: A_Neh
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


# PART ONE 
dataFrameCsv = pandas.read_csv('passengerData.csv')
dataFrameXls = pandas.read_excel('ticketPrices.xlsx')

mergedFiles = pandas.merge(dataFrameCsv, dataFrameXls, on='TicketType')
sorted_df = mergedFiles.sort_values(by='Age', ascending=False)
oldest_person = sorted_df.iloc[0]
print(oldest_person)

plt.figure(figsize=(10, 6))
plt.scatter(sorted_df['Age'], sorted_df['Fare'])
plt.title('Age vs Ticket Price')
plt.xlabel('Age')
plt.ylabel('Ticket Price')
plt.grid(True)
plt.show()

filtered_df = sorted_df[(sorted_df['Sex'] == 'female') & 
                       (sorted_df['Age'] >= 40) & 
                       (sorted_df['Age'] <= 50) & 
                       (sorted_df['Fare'] >= 40)]

plt.figure(figsize=(10, 6))
plt.scatter(filtered_df['Age'], filtered_df['Fare'])
plt.title('Age vs Fare for Female Passengers Aged 40 to 50 with Fare >= 40')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.grid(True)
plt.show()

#PART ONE END

# PART TWO 

titanicDataFrame = pandas.read_csv('titanicSurvival_m.csv')
titanicDataFrame0s = pandas.read_csv('titanicSurvival_m.csv')
titanicDataFrameMeans = pandas.read_csv('titanicSurvival_m.csv')
#print(titanicDataFrame.info())
missing_values_count = titanicDataFrame.isnull().sum()
#print(missing_values_count)
descriptive_states = titanicDataFrame.describe()
print(descriptive_states)

titanicDataFrame0s['Age'].fillna(0, inplace=True)
titanicDataFrame0s['Fare'].fillna(0, inplace=True)

# plt.figure(figsize=(10, 6))
# plt.scatter(titanicDataFrame0s['Age'], titanicDataFrame0s['Fare'])
# plt.title('Age vs Fare')
# plt.xlabel('Age')
# plt.ylabel('Fare')
# plt.grid(True)
# plt.show()

age_mean = titanicDataFrameMeans['Age'].mean()
fare_mean = titanicDataFrameMeans['Fare'].mean()

titanicDataFrameMeans['Age'].fillna(age_mean, inplace=True)
titanicDataFrameMeans['Fare'].fillna(fare_mean, inplace=True)

# plt.figure(figsize=(10, 6))
# plt.scatter(titanicDataFrameMeans['Age'], titanicDataFrameMeans['Fare'])
# plt.title('Age vs Fare')
# plt.xlabel('Age')
# plt.ylabel('Fare')
# plt.grid(True)
# plt.show()

plt.figure(figsize=(20, 10))

# Create the first subplot for the scatter plot with missing values replaced by 0
plt.subplot(1, 2, 1)  # (rows, columns, panel number)
plt.scatter(titanicDataFrame0s['Age'], titanicDataFrame0s['Fare'])
plt.title('Age vs Fare (Missing Values Replaced by 0)')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.grid(True)

# Create the second subplot for the scatter plot with missing values replaced by mean
plt.subplot(1, 2, 2)
plt.scatter(titanicDataFrameMeans['Age'], titanicDataFrameMeans['Fare'])
plt.title('Age vs Fare (Missing Values Replaced by Mean)')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.grid(True)

plt.tight_layout()  # Adjusts the spacing between the two plots for better readability
plt.show()

# PART TWO END 

# PART THREE 

tbDf = pandas.read_csv('TB_burden_countries_2014-09-29_1.csv')
