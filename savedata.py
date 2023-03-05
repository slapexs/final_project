import pandas as pd

class Savedata:
    def __init__(self, df, cluster:list, company_id:list, cluster_name:list) -> None:
        self.dataframe = df
        self.cluster_label = cluster
        self.company_id = company_id
        self.cluster_name = cluster_name
    
    def save_to_csv(self, path:str, filename:str, index:bool):
        self.dataframe['cluster'] = self.cluster_label
        self.dataframe['company_id'] = self.company_id
        self.dataframe['cluster_name'] = self.cluster_name
        self.dataframe.to_csv(f'{path}/{filename}.csv', mode='w', index=index)
    
    def view_column_name(self):
        self.dataframe['cluster'] = self.cluster_label
        return self.dataframe.columns
