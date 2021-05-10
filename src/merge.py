# Importing libraries
import numpy as np # array and vector manipulation
import pandas as pd # data manipulation
import csv

# Copy file class file with oo metrics and test files with test smells 
testsmells_class_data = pd.read_csv("../Dados/Compilado/test-smell.csv")
test_data = pd.read_csv("../Dados/Compilado/metrics.csv")

# Columns of the dataframe
test_data_lines = test_data.shape[0]
testsmells_class_data_lines = testsmells_class_data.shape[0]
    
# Joining test smells and metrics
joined_data_test = pd.merge(test_data, testsmells_class_data, on="Method")
joined_data_test = pd.DataFrame.drop_duplicates(joined_data_test)

# Writing the csv
joined_data_test.to_csv('../Dados/Compilado/TotalTest1.csv', mode='a', index = False, header=True)
