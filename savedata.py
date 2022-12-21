import pandas as pd

class Savedata:
    def __init__(self, df, cluster:list) -> None:
        self.dataframe = df
        self.cluster_label = cluster
    
    def save_to_csv(self, path:str, filename:str, index:bool):
        self.dataframe['cluster'] = self.cluster_label
        self.dataframe.to_csv(f'{path}/{filename}.csv', mode='w', index=index)
    
    def view_column_name(self):
        self.dataframe['cluster'] = self.cluster_label
        return self.dataframe.columns
