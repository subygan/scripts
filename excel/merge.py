import pandas as pd

df = pd.read_excel (r'./application.xlsx', sheet_name='Form Responses 1')
print (df)

df = pd.read_excel (r'./master.xlsx', sheet_name='Sheet1')
print (df)