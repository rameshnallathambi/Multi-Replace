import pandas as pd

df = pd.read_excel('Multi replace.xlsx', sheet_name='Sheet1')

file = open('BeforeReplace.txt')
contents = file.read()
replaced_contents=contents
for i in df.index:
    replaced_contents = replaced_contents.replace(df['As-Is'][i],str(df['To-Be'][i]))

with open('AfterReplace.txt','w') as file1:
    file1.write(replaced_contents)