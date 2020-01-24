import pandas as pd

# benodigd exportbestand uit OSX met daarin tenminste de volgende kolommen Issue ID, wrapper naam
df = pd.read_csv("issues (20200109).csv")
print (df.columns)
#bepaal unieke issues, op basis van de issue ID column.
unieke_issues=df.Issue_Id.unique()
print('Van de', len(unieke_issues), 'unieke issues')

wrapper_lijst=[
'NL BIS Architectuur',
'NL BIS BLS Income',
'NL BIS BLS Object',
'NL BIS CSS',
'NL BIS D&I',
'NL BIS Finance Data',
'NL BIS ITSM',
'NL BIS Model Development en Run',
'NL BIS MT',
'NL BIS Online',
'NL BIS PCO',
'NL BIS Platform management',
'NL BIS SEA',
'NL BIS Security'
]

i=1
j=0
gevonden_issues = [] #make list of 0 length

for s in unieke_issues:
    subset=df.loc[df['Issue_Id'] == s]
    selectie=subset.loc[subset['Title'].isin(wrapper_lijst)]
    if selectie.shape[0] == 0: 
        #voeg waarde toe aan array met gevonden issue
        gevonden_issues.append(s)
        j=j+1   
    i=i+1
    
print ('Hebben er',j, 'niet de juiste wrapper')
print('Het betreft de volgende issue:')
for item in gevonden_issues:
    print (item)
    

