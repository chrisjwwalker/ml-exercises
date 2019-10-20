import pandas as pd

class DataFileLoader:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path

    def load_file(self):
        return pd.read_csv(self.data_file_path)


