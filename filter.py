import pandas as pd
import openpyxl
import xlrd
from openpyxl.workbook import Workbook

path='D:\data\regions.xlsx'
df_excel = pd.read_excel(path)
#df_csv = pd.read_csv("Names.cs")
#df_txt=pd.read.csv ("data.txt")

print(df_excel)