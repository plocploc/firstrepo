import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv("Names.csv", header=None)
df.columns = ['First', 'last', 'Adres', 'City', 'State', 'Area code', 'Income']

df.drop(columns='Adres', inplace = True)

df=df.set_index('Area code')

print(df.loc[8074])