import pandas as pd


class DataTable():
    def __init__(self):
        super(DataTable, self).__init__()
        self.df = pd.DataFrame()

    def add_field(self, name, val_list):
        self.df[name] = val_list

    def get_field(self, name):
        return self.df[name]


class DataPool():
    def __init__(self):
        super(DataPool, self).__init__()
        self.table_dict = {}
    
    def add_table(self, name, table):
        self.table_dict[name] = table

    def add_field(self, name, field, val_list):
        self.table_dict[name][field] = val_list

    def get_table(self, name):
        return self.table_dict[name]
    
    def get_field(self, name, field):
        return self.table_dict[name][field]
