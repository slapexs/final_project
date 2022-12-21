import pandas as pd
import random
from pythainlp.tokenize import word_tokenize
import string

file = './data_csv/allcompany.csv'
spx_char = ['”', '-', '),', '\"', '…', '๗', '​', '​​', '​“', '‎', '–', '‘', '’', '“', '•', '™', '≥']

df = pd.read_csv(file)
new_column_name = [
    'short_company',
    'th_company_name',
    'eng_company_name',
    'type_business',
    'type_technology',
    'product',
    'type_innovation',
    'detail',
    'owner',
    'province_base',
    'address',
    'phone_number',
    'email',
    'website',
    'note',
    'source'
]

# Rename columns
df.columns = new_column_name

# Random sample index
sample_amount = 100
def generate_index(amount:int, sort=True) -> list:
    index_temp = []
    while len(index_temp) < amount:
        rand_temp = random.randint(0, len(df))
        if rand_temp not in index_temp:
            index_temp.append(rand_temp)
    if sort:
        index_temp.sort()
    return index_temp

list_index = [2, 5, 13, 41, 58, 75, 99, 103, 118, 132, 139, 160, 166, 178, 183, 184, 223, 228, 257, 269, 271, 275, 302, 304, 311, 321, 324, 359, 360, 408, 443, 463, 466, 470, 480, 483, 492, 520, 550, 571, 586, 599, 639, 688, 712, 717, 760, 774, 785, 811, 812, 822, 826, 842, 870, 873, 891, 894, 908, 918, 923, 951, 967, 990, 1016, 1038, 1050, 1072, 1082, 1120, 1130, 1132, 1143, 1146, 1156, 1164, 1173, 1192, 1194, 1210, 1212, 1280, 1290, 1301, 1314, 1316, 1321, 1345, 1347, 1358, 1371, 1390, 1434, 1476, 1520, 1529, 1575, 1579, 1623, 1635]

# Create dataframe calculate accuracy
raw_company_detail = []
newmm_detail_tokenize = []
deepcut_detail_tokenize = []
longest_detail_tokenize = []
for i in list_index:
    raw_company_detail.append(df.iloc[i]['detail'])

def tokenize_detail(text:str, engine:str) -> list:
    detail_tokenize = word_tokenize(text, None, engine, False)
    return detail_tokenize

# Clean string
def clean_string(detail:list) -> list:
    temp_clean = []
    for i in detail:
        if i not in string.punctuation and i not in string.digits and i not in spx_char:
            temp_clean.append(i.lower())
    return temp_clean

# Detail tokenize
for idx in list_index:
    temp_detail = df.iloc[idx]['detail']
    newmm_detail_tokenize.append(clean_string(tokenize_detail(temp_detail, 'newmm')))
    deepcut_detail_tokenize.append(clean_string(tokenize_detail(temp_detail, 'deepcut')))
    longest_detail_tokenize.append(clean_string(tokenize_detail(temp_detail, 'longest')))

raw_df = pd.DataFrame({'detail': raw_company_detail})
newmm_df = pd.DataFrame({'detail': newmm_detail_tokenize})
deepcut_df = pd.DataFrame({'detail': deepcut_detail_tokenize})
longest_df = pd.DataFrame({'detail': longest_detail_tokenize})

# Save data to csv
raw_df.to_csv('./accuracy/raw_df.csv', index=False)
newmm_df.to_csv('./accuracy/newmm_df.csv', index=False)
deepcut_df.to_csv('./accuracy/deepcut_df.csv', index=False)
longest_df.to_csv('./accuracy/longest_df.csv', index=False)

print('Data saved!')