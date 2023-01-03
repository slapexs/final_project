import pandas as pd
import random

file = pd.read_csv('./document/editword_clustered_company.csv')

class naming_cluster:

    def appendcompany(self, cluster):
        companies = []
        for i in range(len(file)):
            if file.iloc[i]['cluster'].item() == cluster:
                companies.append(file.iloc[i]['detail'])
        return companies

    def display_samplecompany(self, list_companies:list, amount:int, randoms:bool, display:bool=False):
        companies = []
        rand_index = []
        if randoms:
            rand_index = random.sample(range(0, len(list_companies)), amount)

        if randoms:
            for i in rand_index:
                companies.append(list_companies[i])
        else:
            for i in range(amount):
                companies.append(list_companies[i])
        
        if display:
            for k in range(len(companies)):
                print(f'{k+1}: {companies[k]}')
        else:
            return companies
        
    def len_cluster(self, companies):
        return len(companies)

cluster = 7
companies = naming_cluster().appendcompany(cluster=cluster)
sample = naming_cluster().display_samplecompany(
    list_companies=companies,
    amount=10,
    randoms=True,
    display=True
)
print(f'\n {naming_cluster().len_cluster(companies)}')

'''
    0 = Hardware
    1 = AI
    2 = Online marketing
    3 = IT
    4 = UX/UI design
    5 = Other
    6 = Data
    7 = Software
'''


