##import pandas as pd
##
##excel = pd.DataFrame(columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
##
##df1 = pd.DataFrame(['AIB', 100, 10000, ['Entertainment','Gaming'], 'wwwwww'], columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
##
##excel.append(df1)              
##print(excel)


import pandas as pd

df = pd.DataFrame(columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
df2 = pd.DataFrame([['AIB', 100, 10000, ['Entertainment','Gaming'], 'wwwwww']], columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])

df = df.append(df2)
print (df)
