import pandas as pd

data = './data_csv/combine_company.csv'
df = pd.read_csv(data)

all_group = []
for i in range(len(df)):
    if pd.isna(df.iloc[i]['ประเภทเทคโนโลยี']) == False:
        temp = df.iloc[i]['ประเภทเทคโนโลยี']
        temp1 =temp.split(',')
        for j in temp1:
            all_group.append(j.strip())

# Clean group
list_group = []
for k in all_group:
    if k not in list_group and k != '':
        list_group.append(k.strip())

group_df = pd.DataFrame({'group': list_group})
group_df.to_csv('./data_csv/company_group.csv', mode='w', index=False)
print('success')