import pandas as pd
from managestring import Manage_string
import random

company_file = './data_csv/combine_company.csv'
df = pd.read_csv(company_file)

# Cut string
def test_cut_string(mng:object):
    print('newmm')
    newmm_test = mng.cut_string('newmm')
    print(newmm_test)

    print('\nTLex+')
    tlexplus = mng.cut_with_aiforthai(apikey='n0jwHd2tgKWD65lKJPT4Pd0pYsXYPom7', type='tlexplus')
    print(tlexplus)

    print('\nTLex++')
    tlexplus = mng.cut_with_aiforthai(apikey='n0jwHd2tgKWD65lKJPT4Pd0pYsXYPom7', type='tpos')
    print(tlexplus)

    print('-------------------------------\n')


# Generate sample
sample_amount = 3
def gen_sample(index:list):
    for i in index:
        sampleText = df.iloc[i]['รายละเอียดธุรกิจ']
        mng = Manage_string(sampleText)
        test_cut_string(mng=mng)

# Random data for test
list_index_sample = []
for i in range(sample_amount):
    temp_random = random.randint(0, len(df)-1)
    list_index_sample.append(temp_random) if temp_random not in list_index_sample else ''


gen_sample(list_index_sample)
