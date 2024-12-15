import pandas as pd

df = pd.read_excel('input.xlsx')

print(df)
sorted_df =pd.DataFrame()
sorted_df['list1'] = df['list1'].sort_values(ascending=True).values
sorted_df['list2'] = df['list2'].sort_values(ascending=True).values

print(sorted_df)

sorted_df['sum_of_rows'] = sorted_df['list1']+sorted_df['list2']
print(sorted_df.sum_of_rows.sum())