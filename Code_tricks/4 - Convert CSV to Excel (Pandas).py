import pandas as pd
import numpy as np


# Reading the CSV file
file = pd.read_csv('fail_tests_output.csv')


# Writing and saving excel file
xlsl_file = pd.ExcelWriter('test.xlsx')
file.to_excel(xlsl_file, index=False)
xlsl_file.save()
