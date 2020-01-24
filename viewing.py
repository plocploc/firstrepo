import pandas as pd
from openpyxl.workbook import Workbook


df = pd.read_csv("Names.csv", header=None)


df.columns = ['First', 'last', 'Adres', 'City', 'State', 'Area code', 'bla']

wanted_values = df[['First', 'last', 'bla']]
stored = wanted_values.to_excel('Bla file.xlsx', index=None)