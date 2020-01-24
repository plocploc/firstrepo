import pandas as pd
#import openpyxl
#import xlrd
from openpyxl.workbook import Workbook


df_excel = pd.read_excel("regions.xlsx")
df_csv = pd.read_csv("Names.csv", header=None)
df_txt = pd.read_csv("data.txt", delimiter='\t')

df_csv.columns = ['First', 'last', 'Adres', 'City', 'State', 'Area code', 'bla']

#print(df_excel)
print(df_csv)
#print(df_txt)
df_csv.to_excel('modified.xlsx')   