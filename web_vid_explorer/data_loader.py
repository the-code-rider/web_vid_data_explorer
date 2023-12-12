import pandas as pd
class DataLoader:

    def __init__(self):
        # for web vid : todo : is there a meaning that can be exploited
        self.columns_to_drop = ['page_idx', 'page_dir']

    def load_csv(self, file_path):
        dataframe = pd.read_csv(file_path)
        dataframe.drop(columns=self.columns_to_drop, inplace=True)

